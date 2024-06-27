from langgraph import Graph, Node, Edge

# Initialize a graph
graph = Graph()

# Define nodes for users
user1 = Node(name="User1")
user2 = Node(name="User2")

# Add nodes to the graph
graph.add_node(user1)
graph.add_node(user2)

# Function to create a message node
def create_message_node(sender, text):
    message = Node(name=f"Message from {sender.name}", properties={"text": text})
    graph.add_node(message)
    graph.add_edge(Edge(sender, message))
    return message

# Function to simulate receiving a message
def receive_message(receiver, message):
    graph.add_edge(Edge(message, receiver))

# Create a chain for handling chat interactions
class ChatChain(Chain):
    def __init__(self, graph):
        self.graph = graph

    def send_message(self, sender, receiver, text):
        message = create_message_node(sender, text)
        receive_message(receiver, message)
        return f"{sender.name} to {receiver.name}: {text}"

# Initialize the chat chain with the graph
chat_chain = ChatChain(graph)
def send_message(sender_name, receiver_name, text):
    sender = graph.get_node_by_name(sender_name)
    receiver = graph.get_node_by_name(receiver_name)
    if not sender or not receiver:
        return "Sender or receiver not found."

    response = chat_chain.send_message(sender, receiver, text)
    return response

def get_messages(user_name):
    user = graph.get_node_by_name(user_name)
    if not user:
        return "User not found."
    
    messages = [edge.start.properties["text"] for edge in graph.edges if edge.end == user]
    return messages
if __name__ == "__main__":
    while True:
        print("1. Send a message")
        print("2. View messages")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sender_name = input("Enter sender name: ")
            receiver_name = input("Enter receiver name: ")
            text = input("Enter message text: ")
            print(send_message(sender_name, receiver_name, text))
        
        elif choice == "2":
            user_name = input("Enter user name to view messages: ")
            messages = get_messages(user_name)
            for msg in messages:
                print(msg)
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Please try again.")
