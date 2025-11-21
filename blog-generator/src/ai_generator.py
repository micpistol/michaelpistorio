"""
AI-Powered Blog Post Generator
Uses Claude API to generate blog posts from extracted content
"""

import os
from typing import Dict, Optional
from anthropic import Anthropic


class AIGenerator:
    """Generate blog posts using Claude AI"""

    def __init__(self, config: Dict, api_key: Optional[str] = None):
        self.config = config
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')

        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment or config")

        self.client = Anthropic(api_key=self.api_key)
        self.model = config.get('generation', {}).get('model', 'claude-sonnet-4')

    def generate_blog_post(
        self,
        content: str,
        source_type: str,
        metadata: Dict,
        user_prompt: Optional[str] = None,
        suggested_title: Optional[str] = None
    ) -> Dict[str, str]:
        """
        Generate a blog post from processed content

        Returns:
            {
                'title': str,
                'content': str,  # Markdown formatted
                'excerpt': str,
                'category': str,
                'suggested_tags': list
            }
        """

        # Build the prompt
        system_prompt = self._build_system_prompt()
        user_message = self._build_user_prompt(
            content, source_type, metadata, user_prompt, suggested_title
        )

        # Call Claude API
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.config.get('generation', {}).get('max_tokens', 4000),
                temperature=self.config.get('generation', {}).get('temperature', 0.7),
                system=system_prompt,
                messages=[{
                    "role": "user",
                    "content": user_message
                }]
            )

            # Parse response
            result = self._parse_response(response.content[0].text)
            return result

        except Exception as e:
            raise Exception(f"Error generating blog post: {str(e)}")

    def _build_system_prompt(self) -> str:
        """Build system prompt with style guide and examples"""
        return """You are a skilled technical writer creating blog posts for Michael Pistorio's website about VFX, AI, and computer graphics.

Writing Style:
- Clear, insightful, and accessible to both technical and non-technical readers
- Balance technical depth with readability
- Use concrete examples and analogies
- Forward-thinking but grounded in practical reality
- Avoid excessive jargon; explain complex concepts clearly

Content Structure:
- Strong opening that hooks the reader
- Clear narrative flow with logical progression
- Use headers to organize ideas (H2, H3)
- Include key insights in callout boxes
- End with forward-looking implications ("Trajectory")

Tone:
- Professional but approachable
- Thoughtful and analytical
- Optimistic about technology's potential
- Honest about challenges and limitations

Special Elements:
1. Callouts for key findings:
   > **Key Finding**
   > Important insight here

2. Pull quotes for emphasis:
   > *"A particularly insightful statement worth highlighting"*

3. Trajectory sections for future implications:
   ## Trajectory
   Where this technology or idea is heading...

Format Output As:
```
TITLE: [Blog post title]
CATEGORY: [One of: Introduction, Research, Tutorial, Analysis, Vision]
EXCERPT: [2-3 sentence summary for preview cards]
TAGS: [comma-separated tags]

---

[Full blog post content in Markdown]
```"""

    def _build_user_prompt(
        self,
        content: str,
        source_type: str,
        metadata: Dict,
        user_prompt: Optional[str],
        suggested_title: Optional[str]
    ) -> str:
        """Build user prompt with context"""

        prompt_parts = [
            "Create a blog post from the following source material:\n",
            f"**Source Type:** {source_type}\n"
        ]

        # Add metadata context
        if metadata:
            prompt_parts.append("**Metadata:**\n")
            for key, value in metadata.items():
                if value:
                    prompt_parts.append(f"- {key}: {value}\n")
            prompt_parts.append("\n")

        # Add suggested title if available
        if suggested_title:
            prompt_parts.append(f"**Suggested Title:** {suggested_title}\n\n")

        # Add user's custom instructions
        if user_prompt:
            prompt_parts.append(f"**Additional Instructions:** {user_prompt}\n\n")

        # Add the source content
        prompt_parts.append("**Source Content:**\n\n")
        prompt_parts.append("---\n")
        prompt_parts.append(content)
        prompt_parts.append("\n---\n\n")

        # Add instructions
        prompt_parts.append("""
Please create a compelling blog post based on this material.

Requirements:
1. Extract the key insights and present them clearly
2. Organize the content with a logical flow
3. Add appropriate headers, callouts, and formatting
4. Write an engaging introduction
5. Include a "Trajectory" section discussing future implications
6. Suggest relevant tags
7. Create a concise excerpt for preview

Remember to follow the style guide and format the output correctly.
""")

        return ''.join(prompt_parts)

    def _parse_response(self, response_text: str) -> Dict[str, any]:
        """Parse Claude's response into structured data"""
        lines = response_text.split('\n')

        result = {
            'title': '',
            'category': 'Research',
            'excerpt': '',
            'tags': [],
            'content': ''
        }

        # Parse header section
        content_start = 0
        for i, line in enumerate(lines):
            if line.startswith('TITLE:'):
                result['title'] = line.replace('TITLE:', '').strip()
            elif line.startswith('CATEGORY:'):
                result['category'] = line.replace('CATEGORY:', '').strip()
            elif line.startswith('EXCERPT:'):
                result['excerpt'] = line.replace('EXCERPT:', '').strip()
            elif line.startswith('TAGS:'):
                tags_str = line.replace('TAGS:', '').strip()
                result['tags'] = [t.strip() for t in tags_str.split(',')]
            elif line.strip() == '---':
                content_start = i + 1
                break

        # Extract content (everything after ---)
        if content_start > 0:
            result['content'] = '\n'.join(lines[content_start:]).strip()
        else:
            # Fallback if format is different
            result['content'] = response_text

        return result

    def refine_post(self, current_content: str, feedback: str) -> str:
        """Refine an existing blog post based on feedback"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                temperature=0.7,
                messages=[{
                    "role": "user",
                    "content": f"""Please refine the following blog post based on this feedback:

**Feedback:** {feedback}

**Current Blog Post:**
{current_content}

**Instructions:**
- Address the feedback while maintaining the overall structure
- Keep the same writing style and tone
- Return only the refined blog post content (markdown)
"""
                }]
            )

            return response.content[0].text.strip()

        except Exception as e:
            raise Exception(f"Error refining blog post: {str(e)}")
