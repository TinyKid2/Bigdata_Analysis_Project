import streamlit as st

# 이 부분에 st.set_page_config 명령을 배치하세요.
st.set_page_config(page_title="응급실 통계 시스템", page_icon="🚑", layout="wide")

menu_selection = st.sidebar.selectbox("메뉴 선택", ["HOME", "응급실 이용 데이터 분석","전국 응급 시설 및 의료진 현황"])


# HOME 페이지
if menu_selection == "HOME":
    st.title("🚑ERDS")
    st.write("응급실 통계 시스템 ERDS에 오신 것을 환영합니다.")
    st.write("\n")
    st.info(
        '''
        ERDS는 지역별 응급실 이용 현황 및 응급 시설 및 인력과 관련한 통계 자료를 제공해 주는 시스템입니다. \n
        더 나은 서비스를 제공하기 위해 최선을 다하겠습니다.
        '''
    )


# 응급실 이용 데이터 분석 페이지
if menu_selection == "응급실 이용 데이터 분석":
    st.write("## 응급실 이용 데이터 분석")
    st.write("응급실 이용 데이터 분석 페이지입니다.")
    st.write("\n")

    checkboxes = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

    # 3줄로 나누어진 열을 생성
    num_columns = 3
    columns = [st.columns(num_columns) for _ in range(len(checkboxes) // num_columns + 1)]

    # 각 체크박스에 대한 이미지 경로 리스트
    image_paths = {
        '서울': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/1. 서울.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/1. 서울.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/1. 서울.png'
        ],
        '부산': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/2. 부산.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/2. 부산.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/2. 부산.png'
        ],
        '대구': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/3. 대구.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/3. 대구.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/3. 대구.png'
        ],
        '인천': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/4. 인천.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/4. 인천.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/4. 인천.png'
        ],
        '광주': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/5. 광주.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/5. 광주.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/5. 광주.png'
        ],
        '대전': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/6. 대전.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/5-1. 대전.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/5-1. 대전.png'
        ],
        '울산': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/7. 울산.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/6. 울산.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/6. 울산.png'
        ],
        '세종': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/8. 세종.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/7. 세종.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/7. 세종.png'
        ],
        '경기': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/9. 경기.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/8. 경기.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/8. 경기.png'
        ],
        '강원': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/10. 강원.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/9. 강원.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/9. 강원.png'
        ],
        '충북': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/11. 충북.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/10. 충북.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/10. 충북.png'
        ],
        '충남': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/12. 충남.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/11. 충남.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/11. 충남.png'
        ],
        '전북': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/13. 전북.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/12. 전북.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/12. 전북.png'
        ],
        '전남': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/14. 전남.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/13. 전남.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/13. 전남.png'
        ],
        '경북': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/15. 경북.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/14. 경북.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/14. 경북.png'
        ],
        '경남': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/16. 경남.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/15. 경남.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/15. 경남.png'
        ],
        '제주': [
            '/Users/mac/Desktop/빅데이터 프로젝트/project data/인구수/17. 제주.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 응급실 사용 현황(성별, 연령)/16. 제주.png', '/Users/mac/Desktop/빅데이터 프로젝트/project data/지역별 중증 환자 수 best 5 항목/16. 제주.png'
        ],
    }

    # 각 체크박스에 대한 조건을 추가하여 이미지 출력
    for i, city in enumerate(checkboxes):
        col_idx = i // num_columns
        if columns[col_idx][i % num_columns].checkbox(f"{city}"):
            # 체크박스 인덱스에 대응하는 이미지 리스트
            images_for_city = image_paths[city]
            for j, image_path in enumerate(images_for_city):
                columns[col_idx][i % num_columns].image(image_path, use_column_width=True) #caption=f"Image {city} - {j + 1}"



# 전국 응급실 보유 병원 현황 페이지
if menu_selection == "전국 응급 시설 및 의료진 현황":
    st.write("## 전국 응급실 시설 및 의료진 현황")
    st.write("전국 응급실 시설 및 의료진 현황 페이지입니다.")
    st.write("\n")




# 17개의 체크박스 생성
    if st.checkbox("서울"):
        
        
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/1서울/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/1서울/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/1서울/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/1서울/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/1서울/1_5.png')

    if st.checkbox("부산"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/2부산/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/2부산/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/2부산/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/2부산/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/2부산/1_5.png')


    if st.checkbox("대구"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/3대구/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/3대구/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/3대구/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/3대구/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/3대구/1_5.png')

    if st.checkbox("인천"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/4인천/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/4인천/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/4인천/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/4인천/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/4인천/1_5.png')

    if st.checkbox("광주"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/5광주/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/5광주/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/5광주/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/5광주/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/5광주/1_5.png')


    if st.checkbox("대전"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/6대전/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/6대전/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/6대전/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/6대전/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/6대전/1_5.png')


    if st.checkbox("울산"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/7울산/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/7울산/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/7울산/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/7울산/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/7울산/1_5.png')


    if st.checkbox("세종"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/8세종/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/8세종/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/8세종/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/8세종/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/8세종/1_5.png')

    if st.checkbox("경기"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/9경기/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/9경기/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/9경기/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/9경기/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/9경기/1_5.png')


    if st.checkbox("강원"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/10강원/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/10강원/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/10강원/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/10강원/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/10강원/1_5.png')

    if st.checkbox("충북"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/11충북/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/11충북/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/11충북/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/11충북/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/11충북/1_5.png')


    if st.checkbox("충남"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/12충남/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/12충남/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/12충남/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/12충남/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/12충남/1_5.png')

    if st.checkbox("전북"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/13전북/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/13전북/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/13전북/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/13전북/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/13전북/1_5.png')

    if st.checkbox("전남"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/14전남/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/14전남/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/14전남/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/14전남/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/14전남/1_5.png')

    if st.checkbox("경북"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/15경북/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/15경북/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/15경북/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/15경북/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/15경북/1_5.png')


    if st.checkbox("경남"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/16경남/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/16경남/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/16경남/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/16경남/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/16경남/1_5.png')


    if st.checkbox("제주"):
        st.info("[ 응급실 의료진 인력 현황 ]")
        col1,col2 = st.columns(2)
        col1.image('/Users/mac/Downloads/지역별데이터/17제주/1_1.png')
        col2.image('/Users/mac/Downloads/지역별데이터/17제주/1_2.png')
        
        st.write("\n")
        st.info("[ 응급 구조 시설 및 인력 현황 ]")
        col3,col4,col5 = st.columns(3)
        col3.image('/Users/mac/Downloads/지역별데이터/17제주/1_3.png')
        col4.image('/Users/mac/Downloads/지역별데이터/17제주/1_4.png')
        col5.image('/Users/mac/Downloads/지역별데이터/17제주/1_5.png')
    