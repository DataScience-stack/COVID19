# %%
import streamlit as st
import pydeck
import pandas as pd

# 데이터 가져오기
PatientInfo = pd.read_csv('./PatientInfo.csv')
Region = pd.read_csv('./Region.csv')


# 시각화를 위한 데이터 전처리
Regional_Patient = pd.merge(PatientInfo[['patient_id', 'confirmed_date', 'sex', 'age', 'country', 'province', 'city']],
                            Region[['province', 'city', 'latitude', 'longitude']],
                            how='left', on=['province', 'city'])

# 결측 데이텨 처리
Regional_Count = Regional_Patient[['city', 'latitude', 'longitude']].dropna()

# Uber에서 만든 WebGL 기반 대용량 데이터 시각화 도구 Deck.gl을 사용해 시각화
# WebGL : 웹 기반의 그래픽 라이브러리로 웹 브라우저에서 3D 그래픽을 사용할 수 있게 해준다
# 지도 시각화를 위해 layer 스타일 설정
# layerstyle = 'HexagonLayer'
# layerstyle = 'HeatmapLayer'
layerstyle = 'GridLayer'
# layerstyle = 'PointCloudLayer'
# layerstyle = 'CPUGridLayer'
# layerstyle = 'ScreenGridLayer'
layer = pydeck.Layer(layerstyle,
                     Regional_Count,
                     get_position='[longitude, latitude]',
                     auto_highlight=True,
                     elevation_scale=30,
                     pickable=True,
                     elevation_range=[0, 3000],
                     extruded=True,
                     coverage=10,
                     highPrecision=True,
                     material=True)


View_State = pydeck.ViewState(longitude=127.986,
                              latitude=36.165,
                              zoom=7,
                              min_zoom=4,
                              max_zoom=12,
                              pitch=40.5)

# 시각화
r = pydeck.Deck(layers=[layer],
                initial_view_state=View_State)

st.title('코로나 환자 분포 시각화')
st.pydeck_chart(r)
# r = pdk.Deck(layers=[layer], initial_view_state=view_state)
# r.to_html('demo.html')

# %%

# import streamlit as st
# import pydeck
# import pandas as pd
# # 데이터 import
# patientinfo = pd.read_csv('PatientInfo.csv')
# region = pd.read_csv('Region.csv')
# # 지도 시각화에 필요한 데이터만 전처리
# regional_patient = pd.merge(patientinfo[['patient_id','confirmed_date','sex','age','province','city']],
# region[['province','city','latitude','longitude']], how = 'left', on = ['province','city'])
# regional_count = regional_patient[['city','latitude','longitude']].dropna()
# layer = pydeck.Layer(
# 'HexagonLayer',
# regional_count,
# get_position='[longitude, latitude]',
# auto_highlight=True,
# elevation_scale=50,
# pickable=True,
# elevation_range=[0, 3000],
# extruded=True,
# coverage=1)
# view_state = pydeck.ViewState(
# longitude=127.986,
# latitude=36.165,
# zoom=7,
# min_zoom=4,
# max_zoom=12,
# pitch=40.5)
# # Render
# r = pydeck.Deck(layers=[layer], initial_view_state=view_state)
# st.title('코로나 map deploy')
# st.pydeck_chart(r)