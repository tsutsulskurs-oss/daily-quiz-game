import random
import streamlit as st

QUESTIONS = [
  {
    "question": "물을 끓일 때 물의 온도가 계속 올라가다가 끓기 시작하면 어떻게 될까?",
    "choices": [
      "계속 빠르게 올라간다",
      "일정하게 유지되는 동안이 생긴다",
      "갑자기 0도가 된다",
      "물이 얼기 시작한다"
    ],
    "answer": 2
  },
  {
    "question": "컴퓨터에서 파일을 실수로 삭제했을 때 가장 먼저 확인해볼 곳은?",
    "choices": [
      "휴지통",
      "바탕화면",
      "인터넷",
      "키보드"
    ],
    "answer": 1
  },
  {
    "question": "엘리베이터를 이용할 때 먼저 해야 하는 행동은?",
    "choices": [
      "문을 손으로 막기",
      "안쪽으로 뛰어가기",
      "내릴 사람이 먼저 내리도록 기다리기",
      "버튼을 전부 누르기"
    ],
    "answer": 3
  },
  {
    "question": "달력에서 1년은 일반적으로 몇 개월일까?",
    "choices": [
      "10개월",
      "11개월",
      "12개월",
      "13개월"
    ],
    "answer": 3
  },
  {
    "question": "휴대폰에서 '비행기 모드'를 켜면 주로 제한되는 기능은?",
    "choices": [
      "화면 밝기",
      "일부 무선 통신 기능",
      "카메라",
      "계산기"
    ],
    "answer": 2
  },
  {
    "question": "아이스크림을 실온에 오래 두면 어떻게 될까?",
    "choices": [
      "더 단단해진다",
      "녹는다",
      "얼음으로 변한다",
      "색이 반드시 바뀐다"
    ],
    "answer": 2
  },
  {
    "question": "식사를 하기 전에 손을 씻는 가장 중요한 이유는?",
    "choices": [
      "손의 세균과 오염을 줄이기 위해",
      "손을 따뜻하게 하기 위해",
      "손톱을 길게 하기 위해",
      "피부색을 바꾸기 위해"
    ],
    "answer": 1
  },
  {
    "question": "USB 메모리를 안전하게 제거하는 이유로 가장 적절한 것은?",
    "choices": [
      "컴퓨터 화면을 밝게 하려고",
      "데이터 손상을 줄이려고",
      "인터넷을 빠르게 하려고",
      "키보드를 잠그려고"
    ],
    "answer": 2
  },
  {
    "question": "아침에 일어나 갑자기 어지러울 때 가장 좋은 행동은?",
    "choices": [
      "바로 전력질주하기",
      "안전한 곳에서 잠시 앉거나 쉬기",
      "계속 점프하기",
      "눈을 감고 계단 내려가기"
    ],
    "answer": 2
  },
  {
    "question": "냉동식품을 녹인 뒤 다시 얼리는 것을 조심해야 하는 이유는?",
    "choices": [
      "포장이 커지기 때문에",
      "품질과 식품 안전에 문제가 생길 수 있기 때문에",
      "색깔이 반드시 검게 변하기 때문에",
      "무게가 두 배가 되기 때문에"
    ],
    "answer": 2
  },
  {
    "question": "버스에서 교통카드를 사용하는 목적과 가장 가까운 것은?",
    "choices": [
      "요금을 지불하기 위해",
      "버스 속도를 조절하기 위해",
      "문을 열기 위해",
      "좌석을 만드는 기능"
    ],
    "answer": 1
  },
  {
    "question": "노트북을 사용할 때 통풍구를 막으면 생길 수 있는 문제는?",
    "choices": [
      "기기가 과열될 수 있다",
      "인터넷이 자동으로 빨라진다",
      "배터리가 무조건 충전된다",
      "화면이 커진다"
    ],
    "answer": 1
  },
  {
    "question": "공공장소에서 이어폰을 사용할 때 주의할 점은?",
    "choices": [
      "주변 소리를 전혀 들을 수 없게 하기",
      "주변 상황을 확인할 수 있는 정도로 사용하기",
      "항상 최대 음량으로 듣기",
      "한쪽 귀를 막고 다른 쪽도 완전히 차단하기"
    ],
    "answer": 2
  },
  {
    "question": "신호등에서 초록불이 켜졌더라도 주변을 확인해야 하는 이유는?",
    "choices": [
      "차량이나 자전거가 움직일 수 있기 때문에",
      "신호등이 장식이기 때문에",
      "도로가 자동으로 움직이기 때문에",
      "초록색이 위험한 색이기 때문에"
    ],
    "answer": 1
  },
  {
    "question": "온라인 계정의 2단계 인증을 사용하는 가장 큰 이유는?",
    "choices": [
      "로그인 화면을 예쁘게 만들기 위해",
      "계정 보안을 강화하기 위해",
      "인터넷 속도를 높이기 위해",
      "비밀번호를 없애기 위해"
    ],
    "answer": 2
  },
  {
    "question": "도서관에서 책을 빌릴 때 필요한 경우가 많은 것은?",
    "choices": [
      "회원 정보",
      "운전면허증만",
      "요리 도구",
      "운동화"
    ],
    "answer": 1
  },
  {
    "question": "휴대폰 저장 공간이 부족하면 가장 먼저 해볼 만한 방법은?",
    "choices": [
      "필요 없는 파일이나 앱 정리하기",
      "휴대폰을 흔들기",
      "화면을 계속 켜두기",
      "충전기를 바꾸기"
    ],
    "answer": 1
  },
  {
    "question": "비밀번호를 여러 사이트에서 동일하게 사용하면 생길 수 있는 문제는?",
    "choices": [
      "한 곳의 비밀번호가 유출될 경우 다른 계정도 위험해질 수 있다",
      "인터넷 속도가 느려진다",
      "휴대폰 화면이 깨진다",
      "배터리가 더 빨리 충전된다"
    ],
    "answer": 1
  },
  {
    "question": "전자기기의 충전이 완료된 후에도 계속 연결해 놓는 것보다 좋은 습관은?",
    "choices": [
      "필요에 따라 충전 상태를 관리하기",
      "항상 케이블을 여러 개 연결하기",
      "충전기를 물에 담그기",
      "배터리를 일부러 자주 떨어뜨리기"
    ],
    "answer": 1
  },
  {
    "question": "주방에서 칼을 사용할 때 가장 중요한 것은?",
    "choices": [
      "장난하면서 사용하기",
      "주변을 확인하고 안전하게 사용하기",
      "칼날을 손으로 만져보기",
      "뛰면서 사용하기"
    ],
    "answer": 2
  },
  {
    "question": "옷에 음식물이 묻었을 때 일반적으로 가장 좋은 방법은?",
    "choices": [
      "가능하면 빨리 적절한 방법으로 세탁하기",
      "무조건 햇빛에 며칠 두기",
      "더 문질러서 크게 만들기",
      "물에 담근 채로 영원히 두기"
    ],
    "answer": 1
  },
  {
    "question": "집에서 전등을 사용하지 않을 때 끄는 것이 좋은 이유는?",
    "choices": [
      "전기를 절약할 수 있기 때문에",
      "방의 크기가 커지기 때문에",
      "공기가 자동으로 차가워지기 때문에",
      "인터넷이 빨라지기 때문에"
    ],
    "answer": 1
  },
  {
    "question": "대중교통에서 다른 사람의 자리를 맡아주기 위해 가방을 올려두는 행동은?",
    "choices": [
      "다른 사람에게 불편을 줄 수 있다",
      "항상 예의 바른 행동이다",
      "좌석을 두 배로 만든다",
      "교통비를 줄여준다"
    ],
    "answer": 1
  },
  {
    "question": "알림이 너무 많이 오는 앱은 어떻게 관리하는 것이 좋을까?",
    "choices": [
      "필요 없는 알림을 끄거나 줄인다",
      "모든 알림을 무조건 켠다",
      "휴대폰을 계속 재부팅한다",
      "화면을 깨뜨린다"
    ],
    "answer": 1
  },
  {
    "question": "인터넷에서 모르는 사람이 보낸 파일을 받을 때 가장 안전한 행동은?",
    "choices": [
      "바로 실행한다",
      "출처를 확인하고 의심스러운 파일은 열지 않는다",
      "친구에게 무조건 전달한다",
      "파일 이름만 보고 안전하다고 판단한다"
    ],
    "answer": 2
  },
  {
    "question": "운동을 시작하기 전에 가볍게 몸을 준비하는 활동을 하는 이유는?",
    "choices": [
      "몸을 운동에 적응시키기 위해",
      "더 빨리 지치기 위해",
      "물을 마시지 않기 위해",
      "운동 시간을 없애기 위해"
    ],
    "answer": 1
  },
  {
    "question": "공부할 내용을 오래 기억하는 데 도움이 되는 방법은?",
    "choices": [
      "한 번만 보고 끝내기",
      "복습하기",
      "책을 덮고 생각하지 않기",
      "내용을 전혀 이해하지 않기"
    ],
    "answer": 2
  },
  {
    "question": "친구와 의견이 다를 때 가장 좋은 대화 방법은?",
    "choices": [
      "상대방 말을 끊기",
      "서로의 의견을 들어보기",
      "무조건 큰 소리 내기",
      "대화를 바로 포기하기"
    ],
    "answer": 2
  },
  {
    "question": "학교에서 준비물을 잊어버렸다면 가장 적절한 행동은?",
    "choices": [
      "아무 말도 하지 않기",
      "선생님에게 상황을 설명하고 해결 방법을 찾기",
      "다른 사람 물건을 몰래 가져가기",
      "수업을 방해하기"
    ],
    "answer": 2
  },
  {
    "question": "시간을 효율적으로 관리하는 데 도움이 되는 방법은?",
    "choices": [
      "할 일을 우선순위에 따라 정리하기",
      "모든 일을 동시에 시작하기",
      "계획을 전혀 세우지 않기",
      "마감 직전까지 미루기"
    ],
    "answer": 1
  },
  {
    "question": "온라인에서 본 정보가 사실인지 확인하려면?",
    "choices": [
      "제목만 보고 믿는다",
      "여러 신뢰할 만한 출처를 확인한다",
      "댓글 하나만 확인한다",
      "친구가 말했다면 무조건 믿는다"
    ],
    "answer": 2
  },
  {
    "question": "택배 상자를 버릴 때 개인정보가 적힌 부분은 어떻게 하는 것이 좋을까?",
    "choices": [
      "그대로 공개된 상태로 버린다",
      "개인정보가 보이지 않도록 처리한다",
      "사진을 찍어 인터넷에 올린다",
      "주소를 더 크게 적는다"
    ],
    "answer": 2
  },
  {
    "question": "비밀번호를 다른 사람에게 알려주는 것이 위험한 가장 큰 이유는?",
    "choices": [
      "계정이 다른 사람에게 이용될 수 있기 때문에",
      "화면이 작아지기 때문에",
      "인터넷이 느려지기 때문에",
      "휴대폰이 무거워지기 때문에"
    ],
    "answer": 1
  },
  {
    "question": "여러 사람이 사용하는 컴퓨터에서 로그아웃하는 이유는?",
    "choices": [
      "개인 계정을 보호하기 위해",
      "컴퓨터를 더 크게 만들기 위해",
      "화면을 밝게 하기 위해",
      "키보드를 청소하기 위해"
    ],
    "answer": 1
  },
  {
    "question": "길을 걸으며 휴대폰 화면만 계속 보는 행동이 위험한 이유는?",
    "choices": [
      "주변 상황을 놓칠 수 있기 때문에",
      "배터리가 무조건 충전되기 때문에",
      "걸음 수가 줄어들기 때문에",
      "화면이 커지기 때문에"
    ],
    "answer": 1
  },
  {
    "question": "음식을 보관할 때 냉장 보관이 필요한 식품은 적절한 온도에서 보관해야 하는 이유는?",
    "choices": [
      "변질을 늦추기 위해",
      "무게를 늘리기 위해",
      "색을 바꾸기 위해",
      "포장을 크게 만들기 위해"
    ],
    "answer": 1
  },
  {
    "question": "물을 절약하는 좋은 방법은?",
    "choices": [
      "물을 계속 틀어놓기",
      "사용하지 않을 때 수도꼭지를 잠그기",
      "필요 이상으로 물을 받기",
      "물을 일부러 흘려보내기"
    ],
    "answer": 2
  },
  {
    "question": "종이와 플라스틱을 분리배출하는 주된 목적은?",
    "choices": [
      "재활용과 올바른 폐기를 돕기 위해",
      "쓰레기 양을 늘리기 위해",
      "색깔을 맞추기 위해",
      "봉투를 무겁게 만들기 위해"
    ],
    "answer": 1
  },
  {
    "question": "비가 많이 오는 날 도로에서 차량과 거리를 두는 것이 좋은 이유는?",
    "choices": [
      "차량이 평소보다 제동하기 어려울 수 있기 때문에",
      "차량이 반드시 멈추기 때문에",
      "도로가 사라지기 때문에",
      "비가 차량을 움직이기 때문에"
    ],
    "answer": 1
  },
  {
    "question": "날씨가 추울 때 외출하기 전에 확인하면 좋은 것은?",
    "choices": [
      "기온과 날씨 정보",
      "인터넷 게임 점수",
      "냉장고 크기",
      "책상 높이"
    ],
    "answer": 1
  },
  {
    "question": "약을 복용할 때 가장 중요한 것은?",
    "choices": [
      "다른 사람의 약을 따라 먹기",
      "정해진 용법과 용량을 확인하기",
      "맛을 보기 위해 여러 개 먹기",
      "친구가 추천하면 무조건 먹기"
    ],
    "answer": 2
  },
  {
    "question": "집에서 전기 콘센트를 사용할 때 피해야 하는 행동은?",
    "choices": [
      "안전하게 플러그 사용하기",
      "젖은 손으로 만지기",
      "사용하지 않는 기기 확인하기",
      "손상된 전선 확인하기"
    ],
    "answer": 2
  },
  {
    "question": "컴퓨터에서 문서를 저장할 때 파일 이름을 알아보기 쉽게 정하면 좋은 이유는?",
    "choices": [
      "나중에 파일을 쉽게 찾을 수 있어서",
      "컴퓨터가 더 커져서",
      "인터넷 속도가 빨라져서",
      "화면 색이 변해서"
    ],
    "answer": 1
  },
  {
    "question": "발표를 준비할 때 가장 도움이 되는 방법은?",
    "choices": [
      "내용을 전혀 확인하지 않기",
      "미리 연습해보기",
      "발표 직전에 처음 읽기",
      "자료를 모두 외면하기"
    ],
    "answer": 2
  },
  {
    "question": "친구에게 빌린 물건을 사용한 뒤 가장 적절한 행동은?",
    "choices": [
      "그대로 돌려주지 않는다",
      "상태를 확인하고 제때 돌려준다",
      "다른 사람에게 다시 빌려준다",
      "잃어버려도 말하지 않는다"
    ],
    "answer": 2
  },
  {
    "question": "공공장소에서 쓰레기가 생겼을 때 가장 적절한 행동은?",
    "choices": [
      "바닥에 놓고 간다",
      "적절한 쓰레기통에 버린다",
      "다른 사람 자리 위에 둔다",
      "길에 던진다"
    ],
    "answer": 2
  },
  {
    "question": "온라인 게임이나 서비스에서 다른 사람을 존중하는 행동은?",
    "choices": [
      "상대를 계속 괴롭히기",
      "예의 있게 대화하기",
      "개인정보를 공개하기",
      "욕설을 반복하기"
    ],
    "answer": 2
  },
  {
    "question": "중요한 과제를 시작할 때 가장 먼저 하면 좋은 것은?",
    "choices": [
      "과제 내용을 확인하고 필요한 일을 정리하기",
      "무조건 미루기",
      "아무 준비 없이 제출하기",
      "파일을 삭제하기"
    ],
    "answer": 1
  },
  {
    "question": "인터넷에서 무료 이벤트에 당첨되었다는 메시지를 받았을 때 주의해야 할 점은?",
    "choices": [
      "개인정보나 결제 정보를 바로 입력하기",
      "출처와 내용을 먼저 확인하기",
      "친구에게 비밀번호 보내기",
      "링크를 무조건 누르기"
    ],
    "answer": 2
  },
  {
    "question": "잠을 충분히 자는 것이 일상생활에 도움이 되는 이유는?",
    "choices": [
      "휴식과 회복에 도움이 되기 때문에",
      "시간이 멈추기 때문에",
      "공부가 자동으로 끝나기 때문에",
      "모든 문제가 사라지기 때문에"
    ],
    "answer": 1
  }
]

st.set_page_config(page_title="일상 퀴즈 레벨업", page_icon="🎮", layout="centered")

st.markdown("""
<style>
.stApp { background: #f7f9fc; }
.block-container { max-width: 820px; padding-top: 2rem; }
.hero { background: linear-gradient(135deg,#102a56,#2563eb); color:white; padding:26px; border-radius:22px; margin-bottom:18px; }
.panel { background:white; border:1px solid #e5eaf3; border-radius:18px; padding:20px; margin:12px 0; }
.metric { background:white; border:1px solid #e5eaf3; border-radius:14px; padding:12px; text-align:center; }
.small { color:#64748b; font-size:0.9rem; }
div.stButton > button { border-radius:14px; min-height:46px; font-weight:650; }
</style>
""", unsafe_allow_html=True)

def required_exp(level):
    return 30 + (level - 1) * 10

def get_rank(score):
    if score >= 500: return "MASTER 🏆"
    if score >= 400: return "PLATINUM 💎"
    if score >= 300: return "GOLD 🥇"
    if score >= 200: return "SILVER 🥈"
    return "BRONZE 🥉"

def init_game():
    st.session_state.questions = random.sample(QUESTIONS, len(QUESTIONS))
    st.session_state.level = 1
    st.session_state.exp = 0
    st.session_state.score = 0
    st.session_state.coins = 50
    st.session_state.combo = 0
    st.session_state.index = 0
    st.session_state.hint_used = False
    st.session_state.removed = []
    st.session_state.answered = False
    st.session_state.last_result = None
    st.session_state.started = True

if "started" not in st.session_state:
    st.session_state.started = False

st.markdown('<div class="hero"><h1>🎮 일상 퀴즈 레벨업 게임</h1><p>50개의 일상 문제를 풀고 레벨과 랭크를 올려보세요!</p></div>', unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown('<div class="panel"><h3>게임 안내</h3><p>정답을 맞히면 EXP, 점수, 코인을 얻어요.</p><p>연속 정답은 콤보 보너스를 줍니다. 힌트는 20코인이 필요해요.</p><p class="small">총 50문제 · 랜덤 순서 · 진행 상황은 현재 브라우저 세션에서 유지됩니다.</p></div>', unsafe_allow_html=True)
    if st.button("게임 시작하기", type="primary", use_container_width=True):
        init_game()
        st.rerun()
    st.stop()

level = st.session_state.level
exp = st.session_state.exp
score = st.session_state.score
coins = st.session_state.coins
combo = st.session_state.combo
index = st.session_state.index
total = len(st.session_state.questions)

m1, m2, m3 = st.columns(3)
for col, label, value in [
    (m1, "⭐ LEVEL", f"Lv. {level}"),
    (m2, "✨ EXP", f"{exp} / {required_exp(level)}"),
    (m3, "🔥 COMBO", str(combo))
]:
    with col:
        st.markdown(f'<div class="metric"><div class="small">{label}</div><h3>{value}</h3></div>', unsafe_allow_html=True)
m4, m5 = st.columns(2)
with m4:
    st.markdown(f'<div class="metric"><div class="small">🪙 COIN</div><h3>{coins}</h3></div>', unsafe_allow_html=True)
with m5:
    st.markdown(f'<div class="metric"><div class="small">🏆 RANK · 🎯 SCORE</div><h3>{get_rank(score)} · {score}</h3></div>', unsafe_allow_html=True)

if index >= total:
    st.balloons()
    st.markdown('<div class="panel"><h2>🏁 게임 종료!</h2><h3>최종 결과</h3></div>', unsafe_allow_html=True)
    st.write(f"**최종 레벨:** {st.session_state.level}")
    st.write(f"**최종 EXP:** {st.session_state.exp}")
    st.write(f"**최종 점수:** {st.session_state.score}")
    st.write(f"**최종 코인:** {st.session_state.coins}")
    st.write(f"**최종 랭크:** {get_rank(st.session_state.score)}")
    st.write(f"**마지막 콤보:** {st.session_state.combo}")
    if st.button("다시 플레이", type="primary", use_container_width=True):
        init_game()
        st.rerun()
    st.stop()

q = st.session_state.questions[index]
st.progress(index / total, text=f"문제 {index + 1} / {total}")
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.subheader(f"📖 문제 {index + 1}")
st.markdown(f"### {q['question']}")
st.markdown("</div>", unsafe_allow_html=True)

if not st.session_state.answered:
    if not st.session_state.hint_used:
        if st.button("💡 힌트 사용하기 (20 코인)", disabled=st.session_state.coins < 20):
            st.session_state.coins -= 20
            wrong = [i for i in range(len(q["choices"])) if i != q["answer"] - 1]
            st.session_state.removed = [random.choice(wrong)]
            st.session_state.hint_used = True
            st.rerun()
    else:
        st.info("힌트를 사용했어요. 오답 선택지 하나가 제거되었습니다.")

    option_indices = [i for i in range(4) if i not in st.session_state.removed]
    labels = [f"{i+1}. {q['choices'][i]}" for i in option_indices]
    selected_label = st.radio("정답을 선택하세요", labels, index=None, key=f"answer_{index}")
    if st.button("정답 확인", type="primary", use_container_width=True, disabled=selected_label is None):
        selected_index = option_indices[labels.index(selected_label)] + 1
        if selected_index == q["answer"]:
            st.session_state.combo += 1
            gained_exp = 10
            gained_score = 10 + st.session_state.combo * 2
            gained_coins = 5 + st.session_state.combo
            st.session_state.exp += gained_exp
            st.session_state.score += gained_score
            st.session_state.coins += gained_coins
            while st.session_state.exp >= required_exp(st.session_state.level):
                st.session_state.exp -= required_exp(st.session_state.level)
                st.session_state.level += 1
                st.session_state.coins += 20
            st.session_state.last_result = ("correct", gained_exp, gained_score, gained_coins)
        else:
            st.session_state.combo = 0
            st.session_state.last_result = ("wrong", q["answer"], 0, 0)
        st.session_state.answered = True
        st.rerun()
else:
    result = st.session_state.last_result
    if result[0] == "correct":
        st.success(f"🎉 정답입니다! EXP +{result[1]} · SCORE +{result[2]} · COIN +{result[3]}")
        st.info(f"🔥 {st.session_state.combo} COMBO!")
    else:
        st.error(f"아쉽지만 오답이에요. 정답은 {result[1]}번입니다.")
        st.info("콤보가 초기화되었습니다.")
    if st.button("다음 문제로", type="primary", use_container_width=True):
        st.session_state.index += 1
        st.session_state.hint_used = False
        st.session_state.removed = []
        st.session_state.answered = False
        st.session_state.last_result = None
        st.rerun()

st.caption("일상 퀴즈 레벨업 게임 · 총 50문제")
