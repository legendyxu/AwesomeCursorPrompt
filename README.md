# Awesome Cursor Prompts 🤖

[![GitHub stars](https://img.shields.io/github/stars/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/network)
[![GitHub issues](https://img.shields.io/github/issues/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/issues)
[![GitHub license](https://img.shields.io/github/license/legendyxu/AwesomeCursorPrompt)](https://github.com/legendyxu/AwesomeCursorPrompt/blob/main/LICENSE)

A curated collection of specialized prompts designed to supercharge your Cursor AI development experience. These carefully crafted templates enhance your interaction with AI assistants across the entire development lifecycle.

> **Quick Tip** ⚡ Use `@prompt_name.md` to activate any prompt in Cursor's AI text editor!

> **Note** 🚧 This project is under active development. Some categories are planned for future releases.

## Project Structure 📁

```
cursor_prompts/
├── architect/       # Architecture and planning prompts
├── debug/          # Debugging assistance prompts
├── behavior/       # Best practices and code quality prompts
├── research/       # Technical research query templates
├── summary/        # Project documentation prompts
├── testing/        # Test creation prompts                (upcoming)
├── refactor/       # Code optimization prompts           (upcoming)
├── security/       # Security audit prompts              (upcoming)
├── review/         # Code review prompts                 (upcoming)
└── docs/           # Documentation prompts               (upcoming)
```

## Current Features 🎯

### Architecture Planning (`@architect`)
Transform your project ideas into well-structured implementations:
- Requirements gathering and analysis
- Tech stack evaluation and selection
- System design and component planning
- Architecture validation against best practices
- Development roadmap generation

### Debug Assistant (`@debug`)
Your AI pair programmer for solving complex issues:
- Root cause analysis with step-by-step investigation
- Assumption validation and edge case consideration
- Runtime behavior analysis
- Solution suggestions with explanations
- Verification steps for fixes

### Best Practices (`@behavior`)
Maintain high code quality and professional standards:
- Code style and convention enforcement
- Clear naming and organization guidelines
- Safe refactoring suggestions
- Comprehensive documentation practices
- Performance optimization tips

### Research Helper (`@research`)
Efficient technical research and problem-solving:
- Focused technical query formulation
- Relevant documentation discovery
- Solution evaluation framework
- Alternative approach exploration
- Technology comparison assistance

### Project Summary (`@summary`)
Keep your project well-documented and organized:
- Project structure visualization
- Feature and functionality tracking
- Change history documentation
- Issue resolution logging
- Progress monitoring

## Upcoming Features 🔮

### Testing Assistant (`@testing`)
Comprehensive testing support:
- Unit test generation
- Integration test scenarios
- Edge case identification
- Test data generation
- Coverage improvement suggestions

### Refactoring Guide (`@refactor`)
Code quality improvement:
- Pattern implementation
- Performance optimization
- Technical debt reduction
- Code smell detection
- Modernization suggestions

### Security Checker (`@security`)
Security enhancement:
- Vulnerability scanning
- Security best practices
- Authentication review
- Authorization patterns
- Data protection guidelines

### Code Reviewer (`@review`)
Professional code review:
- Style consistency
- Logic validation
- Performance analysis
- Best practice enforcement
- Improvement suggestions

### Documentation Helper (`@docs`)
Clear and comprehensive documentation:
- API documentation
- Usage examples
- Function descriptions
- README generation
- Change documentation

## Getting Started 🚀

1. Clone this repository:
```bash
git clone https://github.com/legendyxu/AwesomeCursorPrompt.git
cd AwesomeCursorPrompt
```

2. Choose a prompt template that matches your task
3. In Cursor, use `@prompt_name` to activate the prompt
4. Follow the structured format for best results

## Usage Example 💡

Here's how to use the debugging prompt:

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

The AI will provide:
- Root cause analysis
- Common pitfall identification
- Solution suggestions
- Prevention tips


## Contributing 🤝

We welcome contributions! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit (`git commit -m 'Add some AmazingFeature'`)
5. Push (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Found a bug or have a suggestion? [Open an issue](https://github.com/legendyxu/AwesomeCursorPrompt/issues)

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments ✨

- Created to enhance AI-assisted development
- Inspired by real-world development challenges
- Designed for developers of all experience levels
