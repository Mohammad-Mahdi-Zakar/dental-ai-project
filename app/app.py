import gradio as gr
import tensorflow as tf
from PIL import Image
import numpy as np

# 1. تحميل الموديل
model = tf.keras.models.load_model('dental_caries_model_v2.h5')

def predict(img):
    if img is None: return None
    img = img.convert('RGB')
    img = img.resize((224, 224))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(np.copy(img_array))
    score = float(prediction[0][0])
    
    return {
        "Healthy (سليم)": 1 - score,
        "Caries Detected (تسوس)": score
    }

# 2. بناء الواجهة الاحترافية
with gr.Blocks() as demo:
    gr.Markdown("# 🦷 Dental AI Assistant")
    with gr.Row():
        input_img = gr.Image(type="pil", label="ارفع الصورة هنا")
        output_label = gr.Label(num_top_classes=2, label="النتيجة والنسبة")
    with gr.Row():
        btn = gr.Button("Analyze (تحليل)", variant="primary")
        btn.click(fn=predict, inputs=input_img, outputs=output_label)
        clear_btn = gr.Button("Clear (مسح)")
        clear_btn.click(lambda: (None, None), None, [input_img, output_label])

if __name__ == "__main__":
    demo.launch()