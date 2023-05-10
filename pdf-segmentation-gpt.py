import PyPDF2
import openai

# Configuración de la API de OpenAI
openai.api_key = ''
model = 'gpt-3.5-turbo'

# Leer el archivo PDF y extraer el texto
with open('file.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    text = ''
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()

# Dividir el texto en párrafos
segments = text.split("\n")
new_segments = []

# Concatenar párrafos hasta alcanzar el largo lo más cercano posible a 5000 caracteres
current_segment = ""
for segment in segments:
    if len(current_segment + segment) > 5000:
        new_segments.append(current_segment.strip())
        current_segment = ""
    current_segment += " " + segment.strip()
if current_segment:
    new_segments.append(current_segment.strip())

# Eliminar los saltos de línea redundantes
final_segments = []
for segment in new_segments:
    final_segment = ""
    for line in segment.split("\n"):
        line = line.strip()
        if line:
            final_segment += line + "\n"
    if final_segment:
        final_segments.append(final_segment)


# Enviar cada segmento a GPT-3 con una pregunta de "placeholder"
for i, segment in enumerate(new_segments):
    prompt = "Este párrafo corresponde a un documento descriptivo de un proyecto a desarrollar."
    prompt += "Haz una tabla con las funcionalidades indicadas, señalando la categoría a la que pertenece, la complejidad, el esfuerzo, el riesgo y las herramientas asociadas. \n"
    prompt += "El párrafo es': \n"
    # prompt = "Este párrafo pertenece a un documento descriptivo de un producto digital jurídico a desarrollar. "
    # prompt += "Actúa como un Project Manager Senior con experiencia como Tech Lead que debe realizar una estimación de plazos, esfuerzos y complejidad. "
    # prompt += "Escribe una tabla con un listado de las funcionalidades mecionadas. En una primera columna indica la categoría a la que pertenece la "
    # prompt += "funcionalidad, en la segunda columna la funcionalidad, en la tercera la complejidad, en la cuarta el esfuerzo asociado y en la quinta el "
    # prompt += "riesgo técnico o de implementación de esa funcionalidad, en la sexta columna menciona las posibles herramientas, plataformas o "
    # prompt += "infraestructuras tecnológicas asociadas. El párrafo es: "

    prompt += segment
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.3
    )

    if response.choices:
        if response.choices[0].message.content:
            answer = response.choices[0].message.content
        else:
            answer = "No se pudo obtener una respuesta del modelo."
    else:
        answer = "No se pudo obtener una respuesta del modelo."

    # imprimir la posición del segmento y la respuesta generada
    print("Segmento número", i+1)
    #print(prompt)
    print(answer)

