# QA Responder

import ollama

def qa_responder(summary, user_question):
    try:
        response = ollama.chat(
        model='llama3.1',  
        messages=[
        {"role": "system", "content": "Answer based only on the provided summary."},
        {"role": "user", "content": f"Summary: {summary}"},
        {"role": "user", "content": user_question}
        ]
        )

        answer = response['message']['content']
        return answer
    except Exception as e:
        return f"Sorry, I couldn't generate an answer due to: {str(e)}"
