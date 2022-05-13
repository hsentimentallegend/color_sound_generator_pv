import streamlit as st
import cv2
import numpy as np
import winsound


st.title('Color Sound Generator_Plot_Version_0.1')
img_file_buffer = st.camera_input("Take a picture, and Generate Sound with the value of the Color")
if img_file_buffer is not None:

    with open ('test.jpg','wb') as file:   
      file.write(img_file_buffer.getbuffer())
    with open('test.jpg', "rb") as file:
       btn=st.download_button(
       label="Download Picture",
       data=file,
       file_name='colorcleanser.jpg',
       mime="application/octet-stream"
       )         
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    height, width, ch = cv2_img.shape


    size = width * height

    l=0
    b_ave=0; g_ave=0; r_ave=0

    for i in range(height):
        for j in range(width):
            
            if(cv2_img[i,j,0] != 0 or cv2_img[i,j,1] != 0 or cv2_img[i,j,2] != 0 ):
                l+=1    
                b_ave=b_ave+cv2_img[i,j,0]
                g_ave=g_ave+cv2_img[i,j,1]
                r_ave=r_ave+cv2_img[i,j,2]
         
    b_ave=b_ave/l
    g_ave=g_ave/l
    r_ave=r_ave/l

    print(np.round([b_ave, g_ave, r_ave]))

    

    total=((b_ave + g_ave + r_ave)/3) 
    st.write("over200 to Hi, 200-100 to Mid,under 100 to Low",(int(total)))
    

    value=(int(total))


    if st.button('generate sound-with Synthsyzer'):
       duration_ms=5000 
       if value<200 and value >100: 
        winsound.Beep(1002, duration_ms) #ド(523Hz)

        st.write('## success to Generate Mid!!!')
        st.image('img-aaa.jpg')



       elif value>200:
        winsound.Beep(902, duration_ms) #ド(523Hz)

        st.write('## success to Generate Hi!!!')
        st.image('img-aaa.jpg')


       else : 
        winsound.Beep(1002, duration_ms) #ド(523Hz)
         
        st.write('## success to Generate Low!!!')
        st.image('img-aaa.jpg')

       

    link = '[Share Picture with Instagram](https://www.instagram.com/)'
    st.markdown(link, unsafe_allow_html=True)

    link = '[Website](https://www.mehatasentimentallegend.com/)'
    st.markdown(link, unsafe_allow_html=True)

