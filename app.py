from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

def generate_content(keyword):

    # Dictionary with all your content
    data = {
        "photosynthesis": """Photosynthesis is a biological process by which green plants, algae, and some bacteria convert light energy into chemical energy. 
It mainly takes place in the leaves, where a pigment called chlorophyll captures sunlight. During this process, plants use carbon dioxide from the air and water from the soil to produce glucose (a type of food) and release oxygen as a byproduct. 
Photosynthesis is essential for life on Earth because it provides food for plants and oxygen for living organisms.""",

        "courage": """Courage is the ability to face fear, difficulty, or uncertainty without giving up. 
It is not the absence of fear, but the strength to move forward despite it. 
Courage helps people take risks, make tough decisions, and grow stronger through challenges. 
It can be shown in small everyday actions or in big life-changing moments, and it inspires others to be brave too.""",

        "java": """Java is a popular high-level programming language used to create software applications, websites, and mobile apps. 
It is known for its “write once, run anywhere” feature, which means code written in Java can run on any device with a Java Virtual Machine (JVM). 
Java is object-oriented, secure, and platform-independent, making it widely used in industries for developing enterprise software, Android apps, and large-scale systems. 
Its simplicity, reliability, and strong community support make it a favorite among programmers.""",

        "python": """Python is a high-level, interpreted programming language known for its simplicity and readability. 
It is widely used in web development, data science, artificial intelligence, machine learning, automation, and more. 
Python’s syntax is easy to learn, making it beginner-friendly, while its powerful libraries like NumPy, Pandas, and TensorFlow allow developers to build complex applications efficiently. 
Its versatility, large community support, and cross-platform compatibility make Python one of the most popular programming languages today.""",

        "cancer": """Cancer is a disease in which some body cells grow uncontrollably and spread to other parts of the body. 
Normally, cells grow, divide, and die in a regulated way, but in cancer, this process malfunctions. 
There are many types of cancer, such as lung cancer, breast cancer, and skin cancer. 
Causes can include genetics, lifestyle factors, infections, or exposure to harmful chemicals. 
Early detection, treatment like surgery, chemotherapy, or radiation, and healthy lifestyle choices can improve outcomes. 
Awareness and prevention play a key role in fighting cancer."""
    }

    keyword = keyword.lower()

    # Search for content
    for key in data:
        if key in keyword:
            return data[key]

    # Fallback content
    return f"""You searched for '{keyword}'. 
Detailed creative content for this topic will be added soon."""

# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    content = ""

    if request.method == 'POST':
        keyword = request.form['keyword']
        content = generate_content(keyword)

        # Save content to file
        os.makedirs("saved", exist_ok=True)
        with open("saved/output.txt", "w", encoding="utf-8") as f:
            f.write(content)

    return render_template("index.html", content=content)

@app.route('/download')
def download():
    return send_file("saved/output.txt", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)