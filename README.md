# AI Engineering · Learning Notes

> A growing collection of course practice and visual revision notes, organized by course folder.

## Start learning

Start with OpenAI API basics, then move to prompt engineering and advanced techniques. Click a course name to open its notes.

### 1. [OpenAI API](src/openai_api/README.md)

Learn how to send API requests, create and summarize text, use examples in prompts, build conversations, and estimate token costs.

### 2. [Prompt Engineering with the OpenAI API](src/prompt_engineering/README.md)

Learn how to write clear prompts, separate instructions from input text, choose an answer format, and add conditions. Includes visual guides, practice links, and quick revision questions.

### 3. [Advanced Prompt Engineering Techniques](src/advanced_prompt_engineering_techniques/README.md)

Learn how to guide answers with examples, split tasks into steps, check calculations, compare answers, and improve prompts. Includes a mind map, flow diagrams, and recall questions.

## Find your way around

- **This page:** course links and setup steps.
- **Each course README:** topic notes, diagrams, examples, and recall questions.
- **Python files beside the notes:** code you can read and run to practice each topic.

Each course links back to this page, so you can easily switch between topics.

## Coming later

More courses will be added as the learning collection grows:

- Working with Hugging Face
- LLM Ops Concepts
- Working with the OpenAI Responses API
- Introduction to Embeddings with the OpenAI API
- Building AI Applications with Pinecone
- Software Engineering Principles in Python
- Developing LLM Applications with LangChain
- Introduction to Context / MCP

## Shared setup

For the existing OpenAI-based courses, run from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create a local `.env` file with your own key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

The exercises use `load_dotenv()` to load environment variables, and `OpenAI()` reads `OPENAI_API_KEY`. `.env` and `.venv` are already ignored by Git.

Run an exercise using its path:

```bash
python src/openai_api/openai_request.py
python src/prompt_engineering/conditional_prompts.py
```

Running these scripts sends real API requests and may incur charges. The required packages are listed in [requirements.txt](requirements.txt). Check each course README for any extra setup steps.

## Using the notes for revision

Open a course above, look at its learning map, and read the topic you need. Then try the recall questions before opening the answers. Follow the practice links to see how each idea works in code.

Diagrams use Mermaid, which renders on GitHub and in Markdown viewers with Mermaid support.
