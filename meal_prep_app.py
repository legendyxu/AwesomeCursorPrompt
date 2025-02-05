import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Union, Tuple
from dataclasses import dataclass
import io
import csv

# Data Models
@dataclass
class DietaryPreferences:
    """User's dietary preferences and restrictions."""
    allergies: List[str]
    restrictions: List[str]
    portion_multiplier: float
    exclude_ingredients: List[str]

@dataclass
class Ingredient:
    """Represents a single ingredient with its quantities."""
    name: str
    essential_quantity: float
    essential_unit: str
    cooking_quantity: float
    cooking_unit: str
    bulk_quantity: float
    bulk_unit: str

# Column mapping with alternatives
COLUMN_MAPPING = {
    'ingredient': [
        'ingredients',
        'Ingredients',
        'ingredient',
        'Ingredient'
    ],
    'essential_quantity': [
        'quantity',
        'Quantity',
        'essential quantity',
        'Essential Quantity'
    ],
    'essential_unit': [
        'purchasing\nunit',
        'Purchasing\nUnit',
        'purchasing unit',
        'Purchasing Unit'
    ],
    'cooking_quantity': [
        'quantity.1',
        'Quantity.1',
        'cooking quantity',
        'Cooking Quantity'
    ],
    'cooking_unit': [
        'cooking_\nunit',
        'Cooking \nUnit',
        'cooking unit',
        'Cooking Unit'
    ],
    'bulk_quantity': [
        'bulk_purchasing\nquantity',
        'Bulk Purchasing\nQuantity',
        'bulk purchasing quantity',
        'Bulk Purchasing Quantity',
        'Bulk Cooking\nQuantity',
        'bulk cooking quantity'
    ],
    'bulk_unit': [
        'bulk_purchasing_\nunit',
        'Bulk Purchasing \nUnit',
        'bulk purchasing unit',
        'Bulk Purchasing Unit',
        'Bulk Cooking \nUnit',
        'bulk cooking unit'
    ]
}

def normalize_column_name(col: str) -> str:
    """Normalize column name by removing spaces, newlines, and converting to lowercase."""
    return col.strip().lower().replace('\n', '').replace(' ', '')

def find_matching_column(df: pd.DataFrame, target_columns: List[str]) -> Optional[str]:
    """Find the first matching column from the alternatives list."""
    df_cols = set(df.columns)
    for col in target_columns:
        if col in df_cols:
            return col
    
    # Try normalized comparison
    normalized_df_cols = {normalize_column_name(col): col for col in df_cols}
    for col in target_columns:
        normalized_col = normalize_column_name(col)
        if normalized_col in normalized_df_cols:
            return normalized_df_cols[normalized_col]
    
    return None

def create_example_dataframe() -> pd.DataFrame:
    """Create an example DataFrame with the correct format."""
    return pd.DataFrame({
        'Ingredients': ['Black Lentils'],
        'Quantity': [22.5],
        'Purchasing Unit': ['grams'],
        'Quantity.1': [0.794],
        'Cooking Unit': ['ounce'],
        'Bulk Purchasing Quantity': [25.42],
        'Bulk Purchasing Unit': ['ounce'],
        'Ingredient Group': ['Protein'],
        'Special Instructions': ['Rinse before cooking'],
        'Meal Prep Step': ['1'],
        'Meal Prep Box Type': ['Prep']
    })

def preview_csv(file) -> Optional[str]:
    """
    Preview the contents of the CSV file for debugging.
    """
    try:
        # Read first few lines of the file
        content = file.getvalue().decode('utf-8')
        st.write("First 5 lines of uploaded file:")
        lines = content.split('\n')[:5]
        for i, line in enumerate(lines):
            st.code(f"Line {i+1}: {line}")
        
        # Try to detect the delimiter
        dialect = csv.Sniffer().sniff(content)
        st.write(f"Detected delimiter: '{dialect.delimiter}'")
        
        return content
    except Exception as e:
        st.error(f"Error previewing file: {str(e)}")
        return None

@st.cache_data
def load_meal_data(file_content: str) -> Tuple[pd.DataFrame, bool, List[str]]:
    """
    Load and preprocess meal data from CSV content with flexible column mapping.
    """
    try:
        # Try to read with different options if standard reading fails
        try:
            df = pd.read_csv(io.StringIO(file_content))
        except:
            # Try with different encoding
            df = pd.read_csv(io.StringIO(file_content), encoding='utf-8-sig')
        
        if df.empty:
            return pd.DataFrame(), False, []
        
        # Store original columns for debugging
        original_columns = list(df.columns)
        
        # Create a new DataFrame with mapped columns
        processed_df = pd.DataFrame()
        missing_required = []
        
        # Map essential columns
        for target_col, source_alternatives in COLUMN_MAPPING.items():
            matching_col = find_matching_column(df, source_alternatives)
            if matching_col:
                processed_df[target_col] = df[matching_col]
            else:
                # For missing columns, try to derive from other data or use defaults
                if target_col in ['bulk_quantity', 'bulk_unit']:
                    # Use cooking quantities as fallback for bulk
                    cooking_col = find_matching_column(df, COLUMN_MAPPING['cooking_quantity'])
                    cooking_unit_col = find_matching_column(df, COLUMN_MAPPING['cooking_unit'])
                    if cooking_col and cooking_unit_col:
                        processed_df[target_col] = df[cooking_col] if target_col == 'bulk_quantity' else df[cooking_unit_col]
                    else:
                        missing_required.append(target_col)
                else:
                    missing_required.append(target_col)
        
        # Only ingredient name is truly required
        if 'ingredient' not in processed_df.columns:
            st.error("Missing required ingredient column!")
            return df, False, original_columns
        
        # Add additional information columns if they exist
        additional_cols = {
            'notes': ['Special Instructions', 'Special Instruction', 'Notes'],
            'category': ['Ingredient Group', 'Category', 'Group'],
            'step': ['Meal Prep Step', 'Step', 'Prep Step']
        }
        
        for target_col, source_alternatives in additional_cols.items():
            matching_col = find_matching_column(df, source_alternatives)
            if matching_col:
                processed_df[target_col] = df[matching_col]
        
        # If we're missing some quantities, try to fill with reasonable defaults
        if 'essential_quantity' not in processed_df.columns and 'cooking_quantity' in processed_df.columns:
            processed_df['essential_quantity'] = processed_df['cooking_quantity']
            processed_df['essential_unit'] = processed_df['cooking_unit']
        
        if 'cooking_quantity' not in processed_df.columns and 'essential_quantity' in processed_df.columns:
            processed_df['cooking_quantity'] = processed_df['essential_quantity']
            processed_df['cooking_unit'] = processed_df['essential_unit']
        
        # Warning about missing columns that were filled with defaults
        if missing_required:
            st.warning(f"Some columns were missing and filled with defaults: {missing_required}")
        
        return processed_df, True, original_columns
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        return pd.DataFrame(), False, []

def adjust_quantities(
    ingredient: Ingredient,
    preferences: DietaryPreferences
) -> Optional[Ingredient]:
    """
    Adjust ingredient quantities based on user preferences.
    
    Args:
        ingredient: Original ingredient with quantities
        preferences: User's dietary preferences
        
    Returns:
        Adjusted ingredient or None if ingredient should be excluded
    """
    # Check if ingredient is allowed based on preferences
    if (ingredient.name.lower() in [a.lower() for a in preferences.allergies] or
        ingredient.name.lower() in [e.lower() for e in preferences.exclude_ingredients]):
        return None
    
    # Adjust quantities based on portion multiplier
    return Ingredient(
        name=ingredient.name,
        essential_quantity=ingredient.essential_quantity * preferences.portion_multiplier,
        essential_unit=ingredient.essential_unit,
        cooking_quantity=ingredient.cooking_quantity * preferences.portion_multiplier,
        cooking_unit=ingredient.cooking_unit,
        bulk_quantity=ingredient.bulk_quantity * preferences.portion_multiplier,
        bulk_unit=ingredient.bulk_unit
    )

# Streamlit UI
st.title("Personalized Meal Prep Calculator")

# Sidebar for user preferences
st.sidebar.header("Dietary Preferences")

# File upload
uploaded_file = st.file_uploader("Upload your meal recipe (CSV)", type="csv")

if uploaded_file is not None:
    # Preview file contents
    file_content = preview_csv(uploaded_file)
    
    if file_content:
        # Load and display original meal data
        meal_data, is_valid_format, columns = load_meal_data(file_content)
        
        # Show current columns
        st.write("Original columns:", columns)
        
        if not is_valid_format:
            st.error("The uploaded file doesn't match the required format. Here's an example of the correct format:")
            example_df = create_example_dataframe()
            st.write("Example format:")
            st.dataframe(example_df)
            st.download_button(
                label="Download Example CSV",
                data=example_df.to_csv(index=False),
                file_name="example_recipe.csv",
                mime="text/csv"
            )
        
        elif not meal_data.empty:
            st.subheader("Original Recipe")
            st.dataframe(meal_data)
            
            # Safely get ingredient options
            ingredient_options = meal_data['ingredient'].unique()
            
            # Collect user preferences
            allergies = st.sidebar.multiselect(
                "Select your allergies",
                options=ingredient_options,
                default=[]
            )
            
            dietary_restrictions = st.sidebar.multiselect(
                "Select dietary restrictions",
                options=["Vegetarian", "Vegan", "Gluten-free", "Dairy-free"],
                default=[]
            )
            
            portion_multiplier = st.sidebar.slider(
                "Adjust portion size",
                min_value=0.5,
                max_value=3.0,
                value=1.0,
                step=0.1
            )
            
            exclude_ingredients = st.sidebar.multiselect(
                "Exclude specific ingredients",
                options=ingredient_options,
                default=[]
            )
            
            # Create preferences object
            preferences = DietaryPreferences(
                allergies=allergies,
                restrictions=dietary_restrictions,
                portion_multiplier=portion_multiplier,
                exclude_ingredients=exclude_ingredients
            )
            
            # Process button
            if st.button("Calculate Personalized Recipe"):
                st.subheader("Personalized Recipe")
                
                # Convert DataFrame rows to Ingredient objects and process
                adjusted_ingredients = []
                for _, row in meal_data.iterrows():
                    try:
                        ingredient = Ingredient(
                            name=row['ingredient'],
                            essential_quantity=row['essential_quantity'],
                            essential_unit=row['essential_unit'],
                            cooking_quantity=row['cooking_quantity'],
                            cooking_unit=row['cooking_unit'],
                            bulk_quantity=row['bulk_quantity'],
                            bulk_unit=row['bulk_unit']
                        )
                        
                        adjusted = adjust_quantities(ingredient, preferences)
                        if adjusted:
                            adjusted_ingredients.append(adjusted)
                    except KeyError as e:
                        st.error(f"Missing column in data: {e}")
                    except Exception as e:
                        st.error(f"Error processing row: {e}")
                
                # Convert adjusted ingredients back to DataFrame for display
                if adjusted_ingredients:
                    adjusted_df = pd.DataFrame([vars(ing) for ing in adjusted_ingredients])
                    st.dataframe(adjusted_df)
                    
                    # Download button for adjusted recipe
                    csv = adjusted_df.to_csv(index=False)
                    st.download_button(
                        label="Download Adjusted Recipe",
                        data=csv,
                        file_name="adjusted_recipe.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No ingredients remain after applying preferences!")
else:
    st.info("Please upload a meal recipe CSV file to begin.")
    
    # Update the example format display
    st.markdown("""
    ### Expected CSV Format:
    Your CSV should have these essential columns (additional columns are allowed):
    - ingredients
    - quantity (essential amount)
    - purchasing\nunit
    - quantity.1 (cooking amount)
    - cooking_\nunit
    - bulk_purchasing\nquantity
    - bulk_purchasing_\nunit
    
    Optional columns that will be preserved:
    - ingredient_group
    - special_instructions
    - meal_prep_step
    - meal_prep_box_type
    
    Example:
    ```
    ingredients,quantity,purchasing\nunit,quantity.1,cooking_\nunit,bulk_purchasing\nquantity,bulk_purchasing_\nunit
    Black Lentils,22.5,grams,0.794,ounce,25.42,ounce
    ```
    
    💡 The application will map your columns to the internal format automatically!
    """)
    
    # Provide example file for download
    example_df = create_example_dataframe()
    st.download_button(
        label="Download Example CSV Template",
        data=example_df.to_csv(index=False),
        file_name="recipe_template.csv",
        mime="text/csv"
    ) 

print("hellp world")