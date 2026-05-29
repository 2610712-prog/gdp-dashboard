import streamlit as st
import pandas as pd

# 앱 제목 설정
st.title("🔢 재미있는 구구단 웹 앱")
st.markdown("파이썬 코드를 웹 앱으로 변환한 구구단 프로그램입니다.")

# 시각적인 구분을 위한 선
st.divider()

# --- 기능 1: 선택한 단만 보기 ---
st.subheader("🎯 원하는 단 선택해서 보기")

# 사용자에게 라디오 버튼으로 2단~9단 중 하나를 입력받음 (기존 input 역할)
selected_dan = st.radio(
    "출력할 단을 선택하세요:", 
    options=list(range(2, 10)), 
    horizontal=True # 가로로 나열
)

st.info(f"### 📢 {selected_dan}단 출력 결과")

# 기존 사용자의 반복문 로직을 활용하여 선택한 단만 웹에 출력
for j in range(1, 10):
    # print 대신 st.write를 사용해 웹 화면에 텍스트 출력
    st.write(f"**{selected_dan}** × **{j}** = `{selected_dan * j}`")


st.divider()


# --- 기능 2: 2단부터 9단까지 전체 표로 보기 ---
st.subheader("📊 2단~9단 전체 구구단 표")

# 전체 구구단 데이터를 담을 딕셔너리 생성
gugudan_data = {}

# 기존 코드의 2단~9단 이중 반복문 로직 활용
for i in range(2, 10):
    column_data = []
    for j in range(1, 10):
        column_data.append(f"{i}*{j}={i*j}")
    gugudan_data[f"{i}단"] = column_data

# 판다스 데이터프레임으로 변환하여 웹 화면에 깔끔하게 표로 출력
df = pd.DataFrame(gugudan_data, index=[f"×{j}" for j in range(1, 10)])
st.dataframe(df, use_container_width=True)