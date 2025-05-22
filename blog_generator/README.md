# Blog Generator

A Python-based blog generator that uses CrewAI to automatically create blog content. This project demonstrates the use of AI agents working together to generate structured blog content.

## Package Management with uv

This project uses `uv`, a new, fast Python package installer and resolver written in Rust. It's significantly faster than traditional pip and provides better dependency resolution.

### Why uv?

- **Speed**: uv is 10-100x faster than pip
- **Reliability**: Better dependency resolution and conflict handling
- **Compatibility**: Works seamlessly with existing Python projects
- **Modern**: Built with Rust for performance and reliability

### Installing uv

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

### Using uv for this project

```bash
# Create and activate virtual environment
uv venv .venv
source .venv/bin/activate  # On Linux/Mac
# OR
.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -e .
```

## Prerequisites

- Python 3.10 or higher (but less than 3.13)
- pip (Python package installer)
- virtualenv (recommended)

## LLM Configuration

This project uses OpenAI's GPT models through CrewAI. You'll need to set up your API key to use the blog generation features.

### API Key Setup

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a `.env` file in the project root:
```bash
touch .env
```

3. Add your API key to the `.env` file:
```bash
OPENAI_API_KEY=your-api-key-here
```

### Environment Variables

The following environment variables are used in this project:

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `OPENAI_MODEL_NAME` | The model to use (defaults to "gpt-4-turbo-preview") | No |

### Model Configuration

By default, the project uses `gpt-4-turbo-preview` for blog generation. This model provides:
- High-quality content generation
- Better context understanding
- Improved coherence in long-form content

To use a different model, add it to your `.env` file:
```bash
OPENAI_MODEL_NAME=gpt-3.5-turbo  # or any other OpenAI model
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd blog_generator
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# OR
.venv\Scripts\activate  # On Windows
```

3. Install the project and its dependencies:
```bash
pip install -e .
```

## Project Structure

```
blog_generator/
├── src/
│   └── blog_flow/
│       ├── main.py           # Main flow implementation
│       └── crews/
│           └── blog_crew/    # Blog generation crew implementation
├── pyproject.toml            # Project configuration and dependencies
└── README.md                 # This file
```

## Usage

The project provides two main commands:

1. Generate a blog:
```bash
kickoff
```
This command will:
- Generate a random number of sections (between 3 and 6)
- Use the BlogCrew to generate content for each section
- Save the generated blog to `pakistan_history_blog.txt`

2. Plot the flow (if you want to visualize the process):
```bash
plot
```

## How It Works

1. The `BlogFlow` class manages the blog generation process using CrewAI's Flow system
2. The flow consists of three main steps:
   - `generate_section_count`: Determines how many sections the blog will have
   - `generate_blog`: Uses the BlogCrew to create the actual content
   - `save_blog`: Saves the generated content to a text file

## Dependencies

- crewai[tools] >= 0.102.0, < 1.0.0
- pydantic (for data validation)
- Additional dependencies are managed through pyproject.toml

## Development

To modify or extend the project:

1. Make sure you're in the virtual environment
2. Install development dependencies if needed
3. Make your changes in the appropriate files
4. Test your changes using the `kickoff` command

## Output

The generated blog will be saved in `pakistan_history_blog.txt` in the project root directory.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable] 