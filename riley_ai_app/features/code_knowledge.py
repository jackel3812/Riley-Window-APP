"""
CodeKnowledge: Riley's expert coding knowledge engine
- Answers coding questions
- Explains code
- Generates code in multiple languages
- Supports Python, JavaScript, C++, Java, and more
"""
import openai

class CodeKnowledge:
    def __init__(self, openai_api_key=None):
        self.api_key = openai_api_key
        if self.api_key:
            openai.api_key = self.api_key

    def answer(self, question, language="python"):
        """Answer coding questions or generate code in the specified language."""
        prompt = f"You are Riley, an expert AI coding assistant. Answer the following question in {language} and explain your reasoning.\nQuestion: {question}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are Riley, an expert AI coding assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=512,
                temperature=0.2
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[Riley] Sorry, I couldn't answer that due to: {e}"
