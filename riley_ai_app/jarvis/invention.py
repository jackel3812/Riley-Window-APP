def generate_invention_idea(prompt):
    # This function generates invention ideas based on the user's prompt.
    # For demonstration purposes, we'll use a simple template-based approach.
    
    # Example templates for generating invention ideas
    templates = [
        "How about creating a {} that can {}?",
        "What if we designed a {} that helps people {}?",
        "Imagine a {} that allows users to {} in a new way.",
        "Consider developing a {} that can {} more efficiently."
    ]
    
    # Sample inventions and actions
    inventions = ["smart device", "robot", "app", "wearable technology"]
    actions = ["track their health", "connect with others", "automate daily tasks", "learn new skills"]
    
    import random
    
    # Randomly select a template and fill it with random inventions and actions
    template = random.choice(templates)
    invention = random.choice(inventions)
    action = random.choice(actions)
    
    # Generate the invention idea
    idea = template.format(invention, action)
    
    return idea

# Example usage
if __name__ == "__main__":
    user_prompt = "I want to create something innovative."
    invention_idea = generate_invention_idea(user_prompt)
    print(invention_idea)