# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:20:00 2024

@author: Dasein
"""

import streamlit as st
import time
import pandas as pd
import datetime
import random
import folium
from streamlit_folium import st_folium
from streamlit_extras.stylable_container import stylable_container

#网页全局设置
st.set_page_config(
     page_title="果蔬幼儿园主页",
     page_icon=":cat:",
     layout="centered",
     initial_sidebar_state="expanded",
     )

background_css = '''
<style>
body{
     background-image: url('back.jpg');
     background-size: cover;
     }
</style>
'''
st.markdown(background_css, unsafe_allow_html=True)

#网页标题及照片标题字体设置
web_title = """
<style>
p {line-height:1.8;}
</style>
<div style="font-family: 'SimSun', serif;">
<span style="font-size: 30px;">
<text-indent: 2em;>
<strong>
果蔬幼儿园年度纪念册
</div></span></strong></p>
"""

photo_card_title = """
<style>
p {line-height:1.15;}
</style>
<div style="font-family: 'Sylfaen', serif;">
<div style="text-align: center;">
<span style="font-size: 28px;">
<p>
A  Random  Photo  About  Us
</div></span></p>
"""

photo_title = """
<style>
p {line-height:1.5;}
</style>
<div style="font-family: 'SimSun', serif;">
<span style="font-size: 30px;">
<text-indent: 2rem;>
<strong>
果蔬相册
</div></span></strong></p>
"""

#导入随机展示在主页的照片
images_and_captions = [
    {"image": "https://s2.loli.net/2024/11/27/7qDsheEU1A9Y8Lx.jpg", "caption": "24.01.10  红山动物园✌✌"},
    {"image": "https://s2.loli.net/2024/11/27/rtAMLnf15JExGoq.jpg", "caption": "24.01.10  🥬在与水豚会晤"},
    {"image": "https://s2.loli.net/2024/11/27/eNjZ2BgtLWacDQT.jpg", "caption": "24.03.01  🥬(^ω^)与北大楼 =‘x‘=)"},
    {"image": "https://s2.loli.net/2024/11/27/usDaYWHGdZJSUlI.jpg", "caption": "23.11.26  金黄银杏前的🥬"},
    {"image": "https://s2.loli.net/2024/11/26/VilPXqHgF4x7UfJ.jpg", "caption": "23.12.10  一间很小的书店"},
    {"image": "https://s2.loli.net/2024/11/26/6XsULGk1yi5Dp3P.jpg", "caption": "23.12.10  一间很小的书店 · 明信片"},
    {"image": "https://s2.loli.net/2024/11/26/ETDRNemIK5xAw1h.jpg", "caption": "23.12.10  喜鹊bar · 果蔬的第一张拍立得"},
    {"image": "https://s2.loli.net/2024/11/26/vHW2fqjoAVdhGI1.jpg", "caption": "23.12.10  万象天地 · 雪"},
    {"image": "https://s2.loli.net/2024/11/26/tFEzQKxHgSUTDVm.jpg", "caption": "23.12.10  喜鹊bar"},
    {"image": "https://s2.loli.net/2024/11/27/xWzmEdP1rpV5kc2.jpg", "caption": "24.01.09  🍍手持中年🐉"},
    {"image": "https://s2.loli.net/2024/11/28/PtiLljdpuqHN5F4.jpg", "caption": "24.03.09  果蔬couple手机壳"},
    {"image": "https://s2.loli.net/2024/11/28/BaxkEheoPTlfvFR.jpg", "caption": "24.03.08  🥬的节日💐"},
    {"image": "https://s2.loli.net/2024/11/28/8SfIgnad3PkrzAw.jpg", "caption": "24.03.30  🥬抚摸夕阳"},
    {"image": "https://s2.loli.net/2024/11/28/I6dA8oO7gmKYSZQ.jpg", "caption": "24.03.30  天下第一couple"},
    {"image": "https://s2.loli.net/2024/11/28/PCxA6Gg48EOY5pw.jpg", "caption": "24.04.13  晚风来信 · 山阴路的夏天"},
    {"image": "https://s2.loli.net/2024/11/27/xWzmEdP1rpV5kc2.jpg", "caption": "24.01.09  🍍手持中年🐉"},
    {"image": "https://s2.loli.net/2024/11/28/CwaXEmrJsS9KetV.jpg", "caption": "24.06.01  阅江楼观夏"},
    {"image": "https://s2.loli.net/2024/11/28/TCguYREe75M2jd1.jpg", "caption": "24.06.01  阅江楼观夏"},
]

random_choice=random.choice(images_and_captions)

#编辑侧边栏项目
st.sidebar.title(':sheep::cat::dog::pineapple::tomato:')
page=st.sidebar.selectbox('选择页面',('幼儿园大门','果蔬相册','果蔬地图','果蔬小测试'))
if page == "幼儿园大门":
    #
    st.markdown(web_title, unsafe_allow_html=True)
    
    #网页时间模组
    love_advent_day = datetime.date(2023,12,18)
    today = datetime.date.today()
    days_past = today.__sub__(love_advent_day).days
    days_past_str = str(days_past)
    days_count = """
    <div style="font-family: '楷体', serif;">
    <div style="text-align: center; position: fixed; bottom: 0; width: 50%; padding: 30px;">
    <span style="font-size: 15px;">
    今天是 {today}
    <div style="font-family: 'Cambria', serif;"><i>
    From 2023.12.18
    </div></i>
    果蔬幼儿园已经营业 <span style="color: #BA55D3;">{days_past_str}</span> 天~
    </div></span>
    """.format(today=today,days_past_str=days_past_str)
    with st.container(): 
        st.markdown(days_count,unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([1,5,2])
    with col2:
        with st.container(border=True):
                st.markdown(photo_card_title, unsafe_allow_html=True)
                st.image(random_choice['image'],caption=random_choice['caption'],use_column_width=True)
        
    time.sleep(3)
    st.balloons()

if page == "果蔬相册":
    st.header(':camera: :video_camera: :floppy_disk:')
                    
    st.markdown(photo_title, unsafe_allow_html=True)

    # 使用 date_input 显示日历
    selected_year = st.selectbox("选择年份",("2023","2024"))
    if selected_year == "2023":
        selected_month = st.selectbox("选择月份",("十一月","十二月"))
    else:
        selected_month = st.selectbox("选择月份",("一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"))
    
    if selected_year == "2023" and selected_month == "十一月":
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px; text-shadow: 0 0 10px,0 0 20px,0 0 30px;">
        <i><span style="color: #FA9240;">
        2023.11.26
        <br>Our first outing 🍂
        </div></i></span>
        """,unsafe_allow_html=True)
        col1,col2,col3 = st.columns([1,1,1])
        with col1:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/nphg7Z9Hu58ADov.jpg")
                st.image("https://s2.loli.net/2024/11/27/usDaYWHGdZJSUlI.jpg")
                st.image("https://s2.loli.net/2024/11/26/OIaYdyg49QVESMW.jpg")
                st.image("https://s2.loli.net/2024/11/27/6ZxrzKhGknNfI4t.jpg")
                st.image("https://s2.loli.net/2024/11/27/DtgOoqr7uMlZJka.jpg")
        with col2:
            with st.container():
                st.image("https://s2.loli.net/2024/11/26/g1bZNcmriGLykQw.jpg")
                st.image("https://s2.loli.net/2024/11/26/iW7rhEpQJt5OwNu.jpg")
                st.image("https://s2.loli.net/2024/11/27/dFDhqymWBoQnerk.jpg")
                st.image("https://s2.loli.net/2024/11/27/myS3MpDb8JtBIf2.jpg")
                
        with col3:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/f7KZRSlTB3OsenJ.jpg")
                st.image("https://s2.loli.net/2024/11/27/VvdGmgt3CnRh8aQ.jpg")
                st.image("https://s2.loli.net/2024/11/27/uvpKJbwZ3XAexON.jpg")
                st.image("https://s2.loli.net/2024/11/27/Y8bBpDriMv4qgsf.jpg")
    
    if selected_year == "2023" and selected_month == "十二月":
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px;">
        <i>
        2023.12.10</div></i>
        """,unsafe_allow_html=True)
        col1,col2,col3 = st.columns([1,1,1])
        with col1:
            with st.container():
                st.image("https://s2.loli.net/2024/11/26/VilPXqHgF4x7UfJ.jpg")
                st.image("https://s2.loli.net/2024/11/27/cj36iCL5UHybYZK.jpg")
        with col2:
            with st.container():
                st.image("https://s2.loli.net/2024/11/26/ETDRNemIK5xAw1h.jpg")
                st.image("https://s2.loli.net/2024/11/26/6XsULGk1yi5Dp3P.jpg")
                st.image("https://s2.loli.net/2024/11/26/tFEzQKxHgSUTDVm.jpg")
                st.image("https://s2.loli.net/2024/11/27/abI6Q1jWstZ4gvY.jpg")
        with col3:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/bQZJwOfKg1G4tzh.jpg")
                st.image("https://s2.loli.net/2024/11/26/vHW2fqjoAVdhGI1.jpg")
                st.image("https://s2.loli.net/2024/11/26/JD4KfRAMY5r8zZU.jpg")
        
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px; text-shadow: 0 0 10px,0 0 20px,0 0 30px,0 0 40px;">
        <i><span style="color: #C591EA;">
        2023.12.18
        <br>The day of love advent
        </div></i></span>
        """,unsafe_allow_html=True)
        col4,col5,col6 = st.columns([1,1,1])
        with col4:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/jp236sumgnBOdcP.jpg")
                st.image("https://s2.loli.net/2024/11/27/8uaClS4IzGNtJnA.jpg")
        with col5:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/arNsKLY4vlDkAId.jpg")
                st.image("https://s2.loli.net/2024/11/27/tkqG1F23QHNjDBP.jpg")
        with col6:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/IlZMXJR2e4AdNzm.jpg")
                st.image("https://s2.loli.net/2024/11/27/QTiJso8hEnLfPRN.jpg")
                st.image("https://s2.loli.net/2024/11/27/VJlCeHpjvXdoi5P.jpg")
        time.sleep(2)
        st.snow()
        
    if selected_year == "2024" and selected_month == "一月":
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px;">
        <i>
        2024.01.08
        <br>猫咖 & switch 🎮</div></i>
        """,unsafe_allow_html=True)
        col1,col2 = st.columns([1,1])
        with col1:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/xInfOB3j9suoPwp.jpg") 
                st.image("https://s2.loli.net/2024/11/27/kmM8LtDvRPn32uT.jpg")
                st.image("https://s2.loli.net/2024/11/27/5Asau6jHZiO1TPy.jpg")
        with col2:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/JIVfXL7ZEo9CHcw.jpg")
                st.image("https://s2.loli.net/2024/11/27/sgzW7JV2NMFZIPi.jpg")
                st.image("https://s2.loli.net/2024/11/27/DlysroVAuxHPdQf.jpg")
                
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px;">
        <i>
        2024.01.08
        <br>Zoo</div></i>
        """,unsafe_allow_html=True)
        col3,col4,col5 = st.columns([1,1,1])
        with col3:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/hsvjJNiAIDwpaGc.jpg")
                st.image("https://s2.loli.net/2024/11/27/coGNrgsuU94D1MS.jpg")
                st.image("https://s2.loli.net/2024/11/27/iShnIWZ9rdlKxVC.jpg")
                st.image("https://s2.loli.net/2024/11/27/PZa4Y3TeJfWpwM6.jpg")
        with col4:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/CAUXrYHVPucqsFa.jpg")
                st.image("https://s2.loli.net/2024/11/27/rtAMLnf15JExGoq.jpg")
                st.image("https://s2.loli.net/2024/11/27/sGZlimkcY7BjDe1.jpg")
                
        with col5:
            with st.container():
                st.image("https://s2.loli.net/2024/11/27/7qDsheEU1A9Y8Lx.jpg")
                st.image("https://s2.loli.net/2024/11/27/GYBVWHX7N2luk9s.jpg")
                st.image("https://s2.loli.net/2024/11/27/t92adbPrw5nWcuy.jpg")
        
    if selected_year == "2024" and selected_month == "三月":
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px; text-shadow: 0 0 10px,0 0 20px,0 0 30px;">
        <i><span style="color: #FFAEC1;">
        2024.03.10
        <br>Picnic in early spring 🍕
        </div></i></span>
        """,unsafe_allow_html=True)
        col1,col2 = st.columns([1,1])
        with col1:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/vnCsBGXJH251Sgi.jpg")
                st.image("https://s2.loli.net/2024/11/28/eiHcjtarBwqpgZQ.jpg")
                st.image("https://s2.loli.net/2024/11/28/HEgx3eXhy6tFSld.jpg")
                st.image("https://s2.loli.net/2024/11/28/gWE86dhMTow9Vfj.jpg")
        with col2:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/4aLnJRBCUqOTm89.jpg")
                st.image("https://s2.loli.net/2024/11/28/EZuQVXyj28RsdgA.jpg")
                st.image("https://s2.loli.net/2024/11/28/es9rNIoCaMt8PQg.jpg")
        
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px;">
        <i><span style="color: #DE9836;">
        2024.03.30
        <br>镇 江</div></i></span>
        """,unsafe_allow_html=True)
        col3,col4,col5 = st.columns([1,1,1])
        with col3:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/9ErJsVg25qQfy8i.jpg")
                st.image("https://s2.loli.net/2024/11/28/VdDZ43I296pcqF7.jpg")
                st.image("https://s2.loli.net/2024/11/28/Fd5Bb9A1ETgS32p.jpg")
                st.image("https://s2.loli.net/2024/11/28/7kGxTe5jLXpQRoa.jpg")
        with col4:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/I6dA8oO7gmKYSZQ.jpg")
                st.image("https://s2.loli.net/2024/11/28/OtsxNwlRfzPJZ4I.jpg")
                st.image("https://s2.loli.net/2024/11/28/qwJWjpNCMnFzEd6.jpg")
                              
        with col5:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/OZPtvQKEijSCfgG.jpg")
                st.image("https://s2.loli.net/2024/11/28/8c9eDTCjBL2m1zX.jpg")
                st.image("https://s2.loli.net/2024/11/28/2XkW1lfw9gqjOez.jpg")
    
    if selected_year == "2024" and selected_month == "四月":   
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px;">
        <i><span style="color: #7B78A4;">
        2024.04
        <br><div style="text-shadow: 0 0 10px,0 0 20px,0 0 30px,0 0 40px;">颐和路的灯下 </div>
        晚风来信咖啡店
        /愚园
        </div></i></span>
        """,unsafe_allow_html=True)
        col1,col2 = st.columns([1,1])
        with col1:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/ByDQdIbiZRzJWFA.jpg")
                st.image("https://s2.loli.net/2024/11/28/oA4lTsISZhcbKwX.jpg")
                st.image("https://s2.loli.net/2024/11/28/UD47KpdkPIMBtW1.jpg")
        with col2:
            with st.container():
                st.image("https://s2.loli.net/2024/11/28/4RyDxhKJ6afeN9I.jpg")
                st.image("https://s2.loli.net/2024/11/28/f4cC28taNOY7Rp5.jpg")
                st.image("https://s2.loli.net/2024/11/28/PCxA6Gg48EOY5pw.jpg")
                
    if selected_year == "2024" and selected_month == "五月":   
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px; text-shadow: 0 0 10px,0 0 20px,0 0 30px,0 0 40px;">
        <i>
        2024.05.01 ~ 2024.05.03
        </div></i>
        """,unsafe_allow_html=True)
        col3,col4,col5 = st.columns([1,1,1])
        with col3:
            with st.container():
                st.image("")
                st.image("")
                st.image("")
                st.image("")
        with col4:
            with st.container():
                st.image("")
                st.image("")
                st.image("")
                
        with col5:
            with st.container():
                st.image("")
                st.image("")
                st.image("")

    
    
    if selected_year == "2024" and selected_month == "十二月":   
        st.markdown("""
        <div style="font-family: 'Times New Roman'; text-align: center; width: 100%; padding: 50px; text-shadow: 0 0 10px,0 0 20px,0 0 30px,0 0 40px;">
        <i><span style="color: #C591EA;">
        2024.12.18
        <br>Love looks not with the eyes, but with the mind,
        <br>and therefore is winged Cupid painted blind.
        </div></i></span>
        """,unsafe_allow_html=True)
        col3,col4,col5 = st.columns([1,1,1])
        with col3:
            with st.container():
                st.image("")
                st.image("")
                st.image("")
                st.image("")
        with col4:
            with st.container():
                st.image("")
                st.image("")
                st.image("")
                
        with col5:
            with st.container():
                st.image("")
                st.image("")
                st.image("")
        
        
if page == "果蔬地图":
    m = folium.Map(location=[32.0542, 118.7805],
                   zoom_start=15,
                   tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
                   attr='a',
                   control_scale=True)

    # 添加标记到地图
    folium.Marker(
        location=[32.0224, 118.7822],
        popup='Magpie_Bar',
        icon=folium.Icon(icon='fa-solid fa-heart',color="white",icon_color='lightblue', prefix='fa')
        ).add_to(m)
    folium.Marker(
        location=[32.0542, 118.7805],
        popup='Headquarters',
        icon=folium.Icon(icon='fa-solid fa-heart',color='white',icon_color='red', prefix='fa'),
        unsafe_allow_html=True
        ).add_to(m)
    folium.Marker(
        location=[32.012650,118.784000],
        popup='A_small_book_store',
        icon=folium.Icon(icon='fa-solid fa-heart',color="white",icon_color='lightblue', prefix='fa')
        ).add_to(m)
    folium.Marker(
        location=[32.022475,118.779577],
        popup="O'eat_Blossom&Pelican",
        icon=folium.Icon(icon='fa-solid fa-heart',color="white",icon_color='lightblue', prefix='fa')
        ).add_to(m)
    # 在Streamlit应用中展示地图
    st_folium(m, width=750, height=600)
 
if 'clicked' not in st.session_state:
    st.session_state.clicked = False   
    
if 'show' not in st.session_state:
    st.session_state.show = 0
    
if 'mark' not in st.session_state:
    st.session_state.mark = 0

if page == "果蔬小测试":
    st.header('果蔬健康知识小测试🖊')
    if st.button('开始测试'):
        st.session_state.clicked = True
    if st.session_state.clicked:
        answer1 = st.selectbox('卷心菜在世界卫生组织推荐的最佳蔬菜列表中排名第几？',('','第一名','第二名','第三名✌','第四名'))
        if answer1 == '第三名✌':
            answer1_1 = st.selectbox('那么你知道世界卫生组织最推荐的蔬菜是什么吗？',('','芦笋','甜菜','红薯','金针菇'))
            if answer1_1 == '芦笋':
                st.markdown('很接近啦，芦笋排在第二名')
            if answer1_1 == '甜菜':
                st.markdown('呼呼甜菜排在第七名')
            if answer1_1 == '金针菇':
                st.markdown('金针菇排在第十名哦')
            if answer1_1 == '红薯':
                st.markdown('''你是最聪明滴。红薯不仅营养丰富，而且吃红薯能降低血胆固醇，防止亚健康和心脑血管病等“现代病”。
                            我们要吃红薯成为百岁老人o(*￣▽￣*)ブ''')
        answer2 = st.selectbox('🔍判断正误：甜菜块茎的维生素C含量高于甜菜叶。',('','√','×'))
        answer3 = st.selectbox('被称为“水果之王”的一种水果是？',('','火龙果','猕猴桃','哈密瓜','菠萝'))
        if answer3 == '菠萝':
            st.markdown('菠萝是水果之王~尊嘟假嘟(o゜▽゜)o☆')
        answer4 = st.multiselect('100g卷心菜中所含有的高于100g菠萝的营养成分有哪些？',options=['','热量','膳食纤维','钾','胡萝卜素','维生素C','钙'])
        co_answer4 = ['膳食纤维','钾','胡萝卜素','钙']
        answer5 = st.text_input('请输入我们已经去过的城市 ~（城市间用逗号分隔，每个正确答案都能加分捏(●ˇ∀ˇ●)）')
        answer5_list = []
        co_answer5 = ['南京','上海','镇江','嘉兴','滁州','苏州']
        col1,col2,col3 = st.columns([1,2,3.5])
        with col1:
            if st.button('确认提交'):
                st.session_state.show += 1
                if st.session_state.show == 1:
                    #计算答案1是否得分
                    if answer1 == '第三名✌':
                        st.session_state.mark += 10
                    
                    #计算答案2是否得分
                    if answer2 == '×':
                        st.session_state.mark += 10
                    
                    #计算答案3是否得分
                    if answer3 == '猕猴桃':
                        st.session_state.mark += 10
                    
                    #计算答案4的是否得分
                    st.session_state.mark = st.session_state.mark + 10*len(set(set(answer4).intersection(set(co_answer4))))
                                                          
                    #计算答案5是否得分
                    answer5_list = answer5.strip().split('，')
                    #去除答案5列表中可能存在的重复项
                    re_answer5 = []
                    for i in answer5_list:
                        if i not in re_answer5:
                            re_answer5.append(i)
                    st.session_state.mark = st.session_state.mark + 20*len(set(set(re_answer5).intersection(set(co_answer5))))
                if st.session_state.mark >= 100:
                    st.session_state.mark = '100💯'
                result = '你获得了{mark}分'.format(mark=st.session_state.mark)
                st.markdown(result)

                
        with col2:
            if st.button('我要再来一次'):
                st.session_state.show = 0
                st.session_state.mark = 0
        
        with col3:
            if st.session_state.show > 0:
                if st.button('我要学习营养知识！'):
                    with st.expander('“为什么称猕猴桃为‘水果之王’？”'):
                        st.markdown('猕猴桃之所以能被尊称为“水果之王”，更在于其惊人的营养价值。在众多水果中，猕猴桃以其维生素C的超高含量脱颖而出。每100克鲜果中，维生素C的含量可达100至420毫克，这一数字不仅远超甜橙，更是苹果的数十倍之多，几乎在所有水果中名列前茅。维生素C作为人体必需的营养素，对于增强免疫力、促进胶原蛋白合成、保护皮肤健康等方面都发挥着重要作用。')
                        st.markdown('除了维生素C之外，猕猴桃还是一座营养宝库，富含糖类物质、蛋白质、氨基酸等多种有机物，以及钙、铁、锌等人体必需的矿物质。这些营养物质共同作用于人体，不仅能够为身体提供充足的能量，还能促进新陈代谢，维持身体机能的正常运转。特别是猕猴桃中的蛋白水解酶，这种独特的酶类物质能够帮助人体更好地消化肉类食物，预防蛋白质在肠道内的异常凝固，从而减轻肠胃负担。')
                        st.markdown('此外，猕猴桃还含有丰富的纤维素和果胶等膳食纤维成分。这些成分在人体内能够吸水膨胀，增加粪便体积，促进肠道蠕动，有助于预防便秘等肠道问题。同时，它们还能吸附并带走肠道内的有害物质，起到清洁肠道、维护肠道健康的作用。综上所述，猕猴桃以其全面的营养成分和卓越的保健功能，当之无愧地被誉为“水果之王”。')

           
    
    