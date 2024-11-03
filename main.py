# import streamlit as st
# import pandas as pd
# import numpy as np
# from datetime import datetime,timedelta
# from PIL import Image
# import io

# info = """
#         ## Hello，亲爱的SEUer👋
#         ## 欢迎使用我们的数据库指南线上仓库
#         在这里你可以找到我们录制的视频教程，以及对应的数据库资源使用指南😊

#         """

# def main():
#     st.set_page_config(
#         page_title="seu_database')",
#         page_icon="👋",
#     )
#     if 'first_visit' not in st.session_state:
#         st.session_state.first_visit=True
#     else:
#         st.session_state.first_visit=False
#     # 初始化全局配置
#     if st.session_state.first_visit:
#         st.balloons()  
#     st.markdown(info)
    
#     video_info = """
#         ### 🎥1.SEU数据库资源使用视频教程
#             您可以观看下面的视频教程，了解东南大学的数据库资源的使用方法
#         """
#     st.markdown(video_info)
#     video_file = open(r'resource\demo1.mp4', 'rb')
#     video_bytes = video_file.read()
#     st.video(video_bytes)
#     st.divider()

#     pdf_info = """
#         ### 📃2.数据库资源电子指南
#             如果您需要更详细的信息，可以下载我们的数据库资源指南PDF文件
#         """
#     st.markdown(pdf_info)
#     # 打开图像文件
#     image = Image.open('resource\指南图片.png')
#     st.image(image, caption='东南大学数据库资源使用指南', use_column_width=True)

#     col1, col2 = st.columns([2, 1])
#     col1.markdown('##### 点击按钮下载我们的数据库使用指南PDF文件👉')
#     with col2:
#         local_pdf_file_path = r'resource\电子资源指南.pdf'
#         with open(local_pdf_file_path, 'rb') as pdf_file:
#             pdf_bytes = pdf_file.read()
#             pdf_bytes_io = io.BytesIO(pdf_bytes)
        
#         st.download_button(
#             label="下载指南PDF",
#             data=pdf_bytes_io,
#             file_name=f'东南大学数据库资源使用指南.pdf',
#             mime='application/pdf'
#         )
# if __name__ == '__main__':
#     main()


import streamlit as st
from PIL import Image
import io

# 创建一个带有颜色文本的函数
def colored_text(text, color):
    return f'<p style="color:{color};">{text}</p>'

def main():
    st.set_page_config(
        page_title="SEU Database Guide",
        page_icon="👋",
    )
    if 'first_visit' not in st.session_state:
        st.session_state.first_visit = True
    else:
        st.session_state.first_visit = False
    # 初始化全局配置
    if st.session_state.first_visit:
        st.balloons()
    
    # 使用 HTML 来设置中英文双语文本和颜色
    info = """
        <div>
            <h2 style="color:#000000;">Hello，SEUer👋</h2>
            <h2 style="color:#4682B4;">Welcome to our database guide repository</h2>
            
            在这里你可以找到我们录制的视频教程，以及对应的数据库资源使用指南😊
            Here you can find our video tutorials, as well as the corresponding database 
            resource guides.😊
        </div>
        """
    st.markdown(info, unsafe_allow_html=True)
    st.text("")  # 添加一个空行作为分隔
    
    video_info = """
        <div>
            <h3 style="color:#000000;">🎥1.SEU数据库资源使用视频教程</h3>
            <h3 style="color:#4682B4;">🎥1.SEU Database Resource Usage Video Tutorial</h3>
            
            您可以观看下面的视频教程，了解东南大学的数据库资源的使用方法。
            You can watch the video tutorial below to learn how to use the database resources 
            of Southeast University.
        </div>
        """
    st.markdown(video_info, unsafe_allow_html=True)
    st.text("")  # 添加一个空行作为分隔
    
    video_file = open(r'resource\demo1.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.text("")  # 添加一个空行作为分隔
    
    pdf_info = """
        <div>
            <h3 style="color:#000000;">📃2.数据库资源电子指南</h3>
            <h3 style="color:#4682B4;">📃2.Database Resource Electronic Guide</h3>
            
            如果您需要更详细的信息，可以下载我们的数据库资源指南PDF文件
            If you need more detailed information, you can download our database resource
            guide PDF file.
        </div>
        """
    st.markdown(pdf_info, unsafe_allow_html=True)
    st.text("")  # 添加一个空行作为分隔
    
    # 打开图像文件
    image = Image.open('resource\指南图片.png')
    st.image(image, caption='SEU Database Resource Guide', use_column_width=True)
    st.text("")  # 添加一个空行作为分隔

    col1, col2 = st.columns([2, 1])
    col1.markdown(colored_text('点击按钮下载我们的数据库使用指南PDF文件👉', '#FF6347') +
                  colored_text('Click the button to download our database guide PDF file👉', '#4682B4'), unsafe_allow_html=True)
    with col2:
        local_pdf_file_path = r'resource\电子资源指南.pdf'
        with open(local_pdf_file_path, 'rb') as pdf_file:
            pdf_bytes = pdf_file.read()
        pdf_bytes_io = io.BytesIO(pdf_bytes)
        
        st.download_button(
            label="下载指南PDF / Download Guide PDF",
            data=pdf_bytes_io,
            file_name=f'SEU_Database_Resource_Guide.pdf',
            mime='application/pdf'
        )

if __name__ == '__main__':
    main()
