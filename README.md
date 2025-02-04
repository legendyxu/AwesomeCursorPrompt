# Awesome Cursor Prompts 🤖

[![GitHub stars](https://img.shields.io/github/stars/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/network)
[![GitHub issues](https://img.shields.io/github/issues/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/issues)
[![GitHub license](https://img.shields.io/github/license/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/blob/main/LICENSE)

A collection of specialized prompts designed to enhance Cursor AI development workflows. This project provides carefully crafted prompt templates to improve your interaction with AI assistants in various development scenarios, from architecture planning to debugging and documentation.

## 📁 Project Structure

```
cursor_prompts/
├── architect/       # Architecture and planning prompts
├── debug/          # Debugging assistance prompts
├── behavior/       # Best practices and code quality prompts
├── research/       # Technical research query templates
└── summary/        # Project documentation prompts
```

## 🎯 Features

- **Architecture Planning** (`/cursor_prompts/architect/`) - Structured prompts for project architecture design, tech stack selection, and development planning
- **Debug Assistant** (`/cursor_prompts/debug/`) - Systematic approach to debugging issues with thorough analysis and assumption challenging
- **Best Practices** (`/cursor_prompts/behavior/`) - Guidelines for maintaining code quality and professional development practices
- **Research Helper** (`/cursor_prompts/research/`) - Templates for structuring technical research queries
- **Project Summary** (`/cursor_prompts/summary/`) - Automated project documentation and change tracking

## 🚀 Getting Started

Clone this repository to your existing project folder:

```bash
git clone https://github.com/legendyxu/AwesomeCursorPrompt.git
```

Use @ to tag prompt in Cursr's AI text editor.

Each prompt template is designed to be used with AI assistants and follows a specific format:

1. **Architecture Planning**
   - Gathers project requirements
   - Facilitates tech stack decisions
   - Creates structured development plans
   - Validates against existing rules
   - Generates formatted planning documents

2. **Debugging**
   - Promotes thorough analysis
   - Challenges assumptions
   - Considers context and common issues
   - Provides structured problem-solving steps

3. **Best Practices**
   - Ensures code quality
   - Maintains detailed documentation
   - Promotes careful code modifications
   - Includes comprehensive comments for learning

4. **Research Queries**
   - Structures technical search queries
   - Includes relevant context
   - Specifies required technical details
   - Optimizes for human researchers

5. **Project Summary**
   - Generates project structure overviews
   - Documents key features
   - Tracks recent changes
   - Maintains detailed error resolution history

## 💡 Usage

1. Open Cursor and choose the appropriate prompt template for your task
2. Tag the needed prompt in cursor Chat/Composer
3. Use with your preferred LLM

### Example Usage

Here's an example of using the debugging prompt template:

```markdown
@debug I'm encountering a TypeError in my React component:
TypeError: Cannot read property 'map' of undefined

Component code:

```jsx
const UserList = ({ users }) => {
  return (
    <div>
      {users.map(user => <UserCard key={user.id} user={user} />)}
    </div>
  );
}


```

The AI will help analyze:
- Potential causes of undefined users prop
- Common React pitfalls
- Suggested fixes and best practices


## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new prompt templates
- Improve existing templates
- Share best practices
- Report issues

To contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Found a bug or have a suggestion? [Open an issue](https://github.com/legendyxu/AwesomeCursorPrompt/issues)!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgments

- Created to improve AI-assisted development workflows
- Inspired by real-world development challenges
- Designed for both beginners and experienced developers 
