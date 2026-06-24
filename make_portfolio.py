from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from PIL import Image
import os

# ── 폰트 등록 ──
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("MalgunGothic",     os.path.join(FONT_DIR, "malgun.ttf")))
pdfmetrics.registerFont(TTFont("MalgunGothicBold", os.path.join(FONT_DIR, "malgunbd.ttf")))

W, H = A4   # 595.28 x 841.89
INDIGO  = HexColor("#4f46e5")
PURPLE  = HexColor("#7c3aed")
DARK    = HexColor("#0f172a")
MUTED   = HexColor("#64748b")
LIGHT   = HexColor("#f8fafc")
BORDER  = HexColor("#e2e8f0")
GREEN   = HexColor("#10b981")
AMBER   = HexColor("#f59e0b")

SS = "C:/Moa_studio/screenshots"

def gradient_rect(c, x, y, w, h, col1, col2):
    steps = 40
    for i in range(steps):
        t = i / steps
        r = col1.red   + t * (col2.red   - col1.red)
        g = col1.green + t * (col2.green - col1.green)
        b = col1.blue  + t * (col2.blue  - col1.blue)
        c.setFillColorRGB(r, g, b)
        c.rect(x, y + i * h/steps, w, h/steps + 1, fill=1, stroke=0)

def draw_page_header(c, page_num, total=5):
    c.setFillColor(INDIGO)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)
    c.setFont("MalgunGothicBold", 7)
    c.setFillColor(MUTED)
    c.drawRightString(W - 20, 14, f"Moa Studio  ·  {page_num} / {total}")

def draw_tag(c, x, y, text, bg=INDIGO):
    c.setFont("MalgunGothic", 7.5)
    tw = c.stringWidth(text, "MalgunGothic", 7.5)
    pad = 6
    c.setFillColor(bg)
    c.roundRect(x, y - 2, tw + pad*2, 14, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.drawString(x + pad, y + 2, text)
    return tw + pad*2 + 4

# ═══════════════════════════════════════
# PAGE 1 — 표지
# ═══════════════════════════════════════
def page_cover(c):
    gradient_rect(c, 0, 0, W, H, INDIGO, PURPLE)

    # 배경 장식 원
    c.setFillColorRGB(1,1,1, 0.04)
    c.circle(W*0.85, H*0.75, 180, fill=1, stroke=0)
    c.circle(W*0.1,  H*0.2,  120, fill=1, stroke=0)

    # 브랜드
    c.setFont("MalgunGothicBold", 11)
    c.setFillColor(HexColor("#a5b4fc"))
    c.drawString(50, H - 60, "< Moa Studio />")

    # 메인 카피
    c.setFont("MalgunGothicBold", 38)
    c.setFillColor(white)
    c.drawString(50, H - 160, "아이디어를")
    c.drawString(50, H - 210, "실제 서비스로")

    c.setFont("MalgunGothicBold", 38)
    c.setFillColor(HexColor("#c7d2fe"))
    c.drawString(50, H - 260, "만들어 드립니다.")

    # 서브카피
    c.setFont("MalgunGothic", 14)
    c.setFillColor(HexColor("#c7d2fe"))
    c.drawString(50, H - 310, "AI 챗봇 · 모바일 앱 · 자동화 시스템 · 데이터 서비스")

    # 구분선
    c.setStrokeColor(HexColor("#818cf8"))
    c.setLineWidth(1)
    c.line(50, H - 335, W - 50, H - 335)

    # 핵심 수치
    stats = [("10+", "개발 완료 프로젝트"), ("6+", "현재 운영 중 서비스"), ("5+", "AI 연동 서비스")]
    for i, (num, label) in enumerate(stats):
        x = 50 + i * 170
        c.setFont("MalgunGothicBold", 30)
        c.setFillColor(white)
        c.drawString(x, H - 390, num)
        c.setFont("MalgunGothic", 9)
        c.setFillColor(HexColor("#a5b4fc"))
        c.drawString(x, H - 408, label)

    # 하단 소개
    c.setFont("MalgunGothic", 11)
    c.setFillColor(HexColor("#e0e7ff"))
    lines = [
        "개발 경험이 없어도 괜찮습니다.",
        "아이디어만 있으면 함께 구현해 드립니다.",
    ]
    for i, line in enumerate(lines):
        c.drawString(50, 200 - i * 22, line)

    # 연락처
    c.setFillColor(white)
    c.roundRect(50, 100, W - 100, 70, 10, fill=1, stroke=0)
    c.setFont("MalgunGothicBold", 11)
    c.setFillColor(INDIGO)
    c.drawString(70, 150, "문의하기")
    c.setFont("MalgunGothic", 10)
    c.setFillColor(MUTED)
    c.drawString(70, 132, "moadory@gmail.com")
    c.drawString(70, 116, "https://moadory-afk.github.io")

    draw_page_header(c, 1)
    c.showPage()

# ═══════════════════════════════════════
# PAGE 2 — 할 수 있는 것들
# ═══════════════════════════════════════
def page_services(c):
    c.setFillColor(LIGHT)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_page_header(c, 2)

    c.setFont("MalgunGothic", 9)
    c.setFillColor(INDIGO)
    c.drawString(50, H - 55, "// 제공 서비스")

    c.setFont("MalgunGothicBold", 24)
    c.setFillColor(DARK)
    c.drawString(50, H - 88, "이런 것들을 만들어 드릴 수 있어요")

    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(50, H - 100, W - 50, H - 100)

    services = [
        ("🤖", "AI 챗봇 개발",
         "카카오톡, 웹, 앱 어디서든 자연어로 대화하는 AI 챗봇을 만들어 드립니다. 예약 접수, 고객 응대, 자동 안내까지 24시간 자동으로 처리됩니다.",
         ["예약 자동화", "고객 응대", "카카오 연동"]),

        ("📱", "모바일 앱 개발",
         "iOS / Android 동시 출시되는 앱을 개발해 드립니다. 사진 촬영, OCR 인식, 데이터 관리 등 원하는 기능을 앱으로 구현합니다.",
         ["iOS/Android", "OCR", "실시간 데이터"]),

        ("⚡", "업무 자동화 시스템",
         "반복적인 업무를 자동으로 처리하는 시스템을 만들어 드립니다. 데이터 수집, 분류, 알림, 보고서 생성까지 자동화 가능합니다.",
         ["데이터 수집", "자동 알림", "보고서 생성"]),

        ("📊", "데이터 조회 · 분석 서비스",
         "원하는 데이터를 검색하고 시각화하는 웹 서비스를 만들어 드립니다. 공공 API, 사내 데이터 연동 모두 가능합니다.",
         ["공공 API 연동", "시각화", "검색 필터"]),
    ]

    for i, (icon, title, desc, tags) in enumerate(services):
        row = i // 2
        col = i % 2
        x = 50 + col * 255
        y = H - 150 - row * 240

        # 카드 배경
        c.setFillColor(white)
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.8)
        c.roundRect(x, y - 185, 235, 195, 8, fill=1, stroke=1)

        # 아이콘 배경
        c.setFillColor(HexColor("#ede9fe"))
        c.roundRect(x + 14, y - 46, 36, 36, 6, fill=1, stroke=0)
        c.setFont("MalgunGothic", 18)
        c.setFillColor(DARK)
        c.drawString(x + 20, y - 36, icon)

        # 제목
        c.setFont("MalgunGothicBold", 13)
        c.setFillColor(DARK)
        c.drawString(x + 14, y - 68, title)

        # 설명
        c.setFont("MalgunGothic", 8.5)
        c.setFillColor(MUTED)
        words = desc
        lines = []
        line = ""
        for word in words:
            test = line + word
            if c.stringWidth(test, "MalgunGothic", 8.5) > 205:
                lines.append(line)
                line = word
            else:
                line = test
        lines.append(line)
        for j, l in enumerate(lines[:4]):
            c.drawString(x + 14, y - 90 - j * 13, l)

        # 태그
        tx = x + 14
        for tag in tags:
            tw = draw_tag(c, tx, y - 168, tag, HexColor("#ede9fe"))
            c.setFillColor(INDIGO)
            # 태그 텍스트를 다시 그림 (색상 수정)
        tx = x + 14
        for tag in tags:
            c.setFont("MalgunGothic", 7.5)
            tw_val = c.stringWidth(tag, "MalgunGothic", 7.5)
            pad = 6
            c.setFillColor(HexColor("#ede9fe"))
            c.roundRect(tx, y - 170, tw_val + pad*2, 14, 4, fill=1, stroke=0)
            c.setFillColor(INDIGO)
            c.drawString(tx + pad, y - 166, tag)
            tx += tw_val + pad*2 + 4

    c.showPage()

# ═══════════════════════════════════════
# PAGE 3 — 프로젝트 (상단 3개)
# ═══════════════════════════════════════
def draw_project_card(c, x, y, w, h, title, desc, tags, img_path, badge=None, badge_color=GREEN):
    c.setFillColor(white)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 8, fill=1, stroke=1)

    img_h = 110
    # 이미지
    if img_path and os.path.exists(img_path):
        try:
            img = Image.open(img_path)
            iw, ih = img.size
            # 카드 너비에 맞춰 crop
            aspect = iw / ih
            draw_w = w - 0
            draw_h = img_h
            c.saveState()
            c.roundRect(x, y + h - img_h, w, img_h, 8, fill=0, stroke=0)
            c.clipPath(c.beginPath(), fill=0)
            # 이미지 그리기
            c.drawImage(img_path, x, y + h - img_h, width=w, height=img_h,
                       preserveAspectRatio=False, anchor='nw',
                       mask='auto')
            c.restoreState()
        except:
            c.setFillColor(HexColor("#f0f4ff"))
            c.roundRect(x, y + h - img_h, w, img_h, 8, fill=1, stroke=0)
    else:
        c.setFillColor(HexColor("#f0f4ff"))
        c.roundRect(x, y + h - img_h, w, img_h, 8, fill=1, stroke=0)

    # 배지
    if badge:
        c.setFillColor(badge_color)
        c.roundRect(x + 8, y + h - img_h + 8, 40, 13, 3, fill=1, stroke=0)
        c.setFont("MalgunGothic", 6.5)
        c.setFillColor(white)
        c.drawString(x + 11, y + h - img_h + 12, badge)

    # 제목
    c.setFont("MalgunGothicBold", 11)
    c.setFillColor(DARK)
    c.drawString(x + 10, y + h - img_h - 20, title)

    # 설명
    c.setFont("MalgunGothic", 7.5)
    c.setFillColor(MUTED)
    line = ""
    ly = y + h - img_h - 35
    for ch in desc:
        line += ch
        if c.stringWidth(line, "MalgunGothic", 7.5) > w - 22:
            c.drawString(x + 10, ly, line[:-1])
            ly -= 12
            line = ch
    if line:
        c.drawString(x + 10, ly, line)

    # 태그
    tx = x + 10
    ty = y + 12
    for tag in tags[:3]:
        c.setFont("MalgunGothic", 6.5)
        tw = c.stringWidth(tag, "MalgunGothic", 6.5)
        pad = 5
        c.setFillColor(HexColor("#f1f5f9"))
        c.roundRect(tx, ty, tw + pad*2, 12, 3, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.drawString(tx + pad, ty + 2, tag)
        tx += tw + pad*2 + 3

def page_projects1(c):
    c.setFillColor(LIGHT)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_page_header(c, 3)

    c.setFont("MalgunGothic", 9)
    c.setFillColor(INDIGO)
    c.drawString(50, H - 55, "// 개발 사례")

    c.setFont("MalgunGothicBold", 24)
    c.setFillColor(DARK)
    c.drawString(50, H - 88, "실제로 만들고 운영 중인 서비스들")

    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(50, H - 100, W - 50, H - 100)

    projects = [
        ("세상의 모든 불만", "소비자 불만을 AI가 자동 분류·그룹핑해서 기업에 전달하는 모바일 앱",
         ["모바일 앱", "AI 분류", "커뮤니티"], f"{SS}/bulman.jpg", "● 운영중", GREEN),
        ("GogoPar — 골프 스코어 앱", "스코어카드 사진 찍으면 자동으로 핸디캡 계산, 시상까지 처리되는 골프 클럽 관리 앱",
         ["모바일 앱", "OCR", "골프"], f"{SS}/golf.jpg", "● 운영중", GREEN),
        ("식당 AI 예약 챗봇", "카카오톡으로 자연어 예약을 받고, 자동으로 확정 문자까지 발송하는 예약 시스템",
         ["AI 챗봇", "카카오", "예약관리"], f"{SS}/restaurant.jpg", "● 운영중", GREEN),
    ]

    card_w = (W - 100 - 20) / 3
    card_h = 265
    y_start = H - 140

    for i, (title, desc, tags, img, badge, bcol) in enumerate(projects):
        x = 50 + i * (card_w + 10)
        draw_project_card(c, x, y_start - card_h, card_w, card_h,
                         title, desc, tags, img, badge, bcol)

    c.showPage()

# ═══════════════════════════════════════
# PAGE 4 — 프로젝트 (하단 3개)
# ═══════════════════════════════════════
def page_projects2(c):
    c.setFillColor(LIGHT)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_page_header(c, 4)

    c.setFont("MalgunGothic", 9)
    c.setFillColor(INDIGO)
    c.drawString(50, H - 55, "// 개발 사례 계속")

    c.setFont("MalgunGothicBold", 24)
    c.setFillColor(DARK)
    c.drawString(50, H - 88, "다양한 분야에 적용한 경험이 있습니다")

    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(50, H - 100, W - 50, H - 100)

    projects = [
        ("실손보험 청구관리 앱", "병원 영수증 사진 한 장으로 실손보험 청구를 원스톱 자동화하는 앱",
         ["모바일 앱", "OCR", "보험"], f"{SS}/insuarance.jpg", "● 운영중", GREEN),
        ("똥꾸 School", "AI가 오답을 분석하고 1:1 커리큘럼을 설계해주는 수학 코칭 시스템",
         ["AI 교육", "오답 분석", "수능"], f"{SS}/math.jpg", "● 운영중", GREEN),
        ("실거래가 조회 서비스", "국토부 공공 API 연동으로 아파트·빌라 실거래 데이터를 검색하는 웹 서비스",
         ["웹 서비스", "공공 API", "부동산"], f"{SS}/real.jpg", "● 운영중", GREEN),
    ]

    card_w = (W - 100 - 20) / 3
    card_h = 265
    y_start = H - 140

    for i, (title, desc, tags, img, badge, bcol) in enumerate(projects):
        x = 50 + i * (card_w + 10)
        draw_project_card(c, x, y_start - card_h, card_w, card_h,
                         title, desc, tags, img, badge, bcol)

    # 추가 프로젝트 언급
    c.setFillColor(white)
    c.setStrokeColor(BORDER)
    c.roundRect(50, 50, W - 100, 60, 8, fill=1, stroke=1)
    c.setFont("MalgunGothicBold", 10)
    c.setFillColor(DARK)
    c.drawString(70, 92, "그 외에도...")
    c.setFont("MalgunGothic", 9)
    c.setFillColor(MUTED)
    c.drawString(70, 74, "AI 자동매매 시스템, 쇼츠 영상 자동생성, 금융 비교 시스템 등 다양한 프로젝트 경험 보유")

    c.showPage()

# ═══════════════════════════════════════
# PAGE 5 — 문의 / 마무리
# ═══════════════════════════════════════
def page_contact(c):
    gradient_rect(c, 0, 0, W, H, DARK, HexColor("#1e1b4b"))
    draw_page_header(c, 5)

    # 장식
    c.setFillColorRGB(1,1,1,0.03)
    c.circle(W - 80, 120, 150, fill=1, stroke=0)

    c.setFont("MalgunGothic", 9)
    c.setFillColor(HexColor("#a5b4fc"))
    c.drawString(50, H - 60, "// 함께 만들어요")

    c.setFont("MalgunGothicBold", 28)
    c.setFillColor(white)
    c.drawString(50, H - 100, "개발이 필요하신가요?")
    c.setFont("MalgunGothicBold", 28)
    c.setFillColor(HexColor("#c7d2fe"))
    c.drawString(50, H - 140, "편하게 연락주세요.")

    c.setFont("MalgunGothic", 11)
    c.setFillColor(HexColor("#94a3b8"))
    c.drawString(50, H - 175, "아이디어 단계부터 함께 고민하고, 실제 서비스로 만들어 드립니다.")

    # 프로세스
    c.setFont("MalgunGothicBold", 12)
    c.setFillColor(white)
    c.drawString(50, H - 225, "개발 진행 과정")

    steps = [
        ("01", "무료 상담", "어떤 서비스가 필요한지\n자유롭게 말씀해 주세요"),
        ("02", "기획 · 견적", "요구사항을 정리하고\n일정과 비용을 안내드립니다"),
        ("03", "개발 · 테스트", "개발 진행 상황을\n수시로 공유드립니다"),
        ("04", "납품 · 운영", "배포 후에도 유지보수\n지원 가능합니다"),
    ]

    for i, (num, title, desc) in enumerate(steps):
        x = 50 + i * 125
        y = H - 310

        # 번호 원
        c.setFillColor(INDIGO)
        c.circle(x + 18, y + 18, 18, fill=1, stroke=0)
        c.setFont("MalgunGothicBold", 10)
        c.setFillColor(white)
        c.drawCentredString(x + 18, y + 14, num)

        # 화살표
        if i < 3:
            c.setStrokeColor(HexColor("#4f46e5"))
            c.setLineWidth(1)
            c.line(x + 40, y + 18, x + 108, y + 18)
            p = c.beginPath()
            p.moveTo(x+115, y+18)
            p.lineTo(x+107, y+22)
            p.lineTo(x+107, y+14)
            p.close()
            c.setFillColor(INDIGO)
            c.drawPath(p, fill=1, stroke=0)

        c.setFont("MalgunGothicBold", 9)
        c.setFillColor(white)
        c.drawString(x, y - 10, title)
        c.setFont("MalgunGothic", 7.5)
        c.setFillColor(HexColor("#94a3b8"))
        for j, line in enumerate(desc.split('\n')):
            c.drawString(x, y - 24 - j*11, line)

    # 연락처 카드
    c.setFillColor(white)
    c.roundRect(50, 120, W - 100, 160, 12, fill=1, stroke=0)

    c.setFont("MalgunGothicBold", 13)
    c.setFillColor(DARK)
    c.drawString(75, 258, "지금 바로 문의하세요")

    c.setFont("MalgunGothic", 10)
    c.setFillColor(MUTED)
    contacts = [
        ("이메일", "moadory@gmail.com"),
        ("포트폴리오", "https://moadory-afk.github.io"),
    ]
    for i, (label, value) in enumerate(contacts):
        y = 228 - i * 24
        c.setFont("MalgunGothic", 8)
        c.setFillColor(MUTED)
        c.drawString(75, y, label)
        c.setFont("MalgunGothicBold", 10)
        c.setFillColor(DARK)
        c.drawString(150, y, value)

    # 하단 문구
    c.setFont("MalgunGothic", 8)
    c.setFillColor(HexColor("#334155"))
    c.drawCentredString(W/2, 148, "빠른 답변 드리겠습니다. 부담 없이 연락 주세요 :)")

    # 푸터
    c.setFont("MalgunGothic", 7)
    c.setFillColor(HexColor("#475569"))
    c.drawCentredString(W/2, 30, "Moa Studio  ·  moadory@gmail.com  ·  2025")

    c.showPage()


# ═══════════════════════════════════════
# 생성 실행
# ═══════════════════════════════════════
out_path = "C:/Moa_studio/MoaStudio_Portfolio.pdf"
c = canvas.Canvas(out_path, pagesize=A4)
c.setTitle("Moa Studio 포트폴리오")
c.setAuthor("Moa Studio")

page_cover(c)
page_services(c)
page_projects1(c)
page_projects2(c)
page_contact(c)

c.save()
print(f"완료: {out_path}")
