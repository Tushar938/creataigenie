
import openai
openai.api_key = 'sk-None-aKljgbAs8suMFjwDqy17T3BlbkFJ0lytMQBBew01jg5QqwIS'

def summarize_text(text):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Please summarize the following text:\n\n{text}",
            max_tokens=150,  
            temperature=0.5
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    text_to_summarize = input("Enter your text and get it summarized: ")
    summary = summarize_text(text_to_summarize)
    print("Summary:", summary)
