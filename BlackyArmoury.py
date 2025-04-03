import sys
import time
import itertools
import threading


class BlackyArmoury:
    def __init__(self, input_function=None):
        self.menu = {
            "1": ("버그바운티", self.show_bug_bounty),
            "2": ("모의침투 테스트", self.show_pentest),
            "3": ("PAYLOAD", self.show_payloads),
            "4": ("보고서 작성", self.show_report_writing),
            "0": ("종료", self.exit_program)
        }
        self.input_function = input_function or self.default_input_function
        self.loading_done = False

    def default_input_function(self, prompt):
        try:
            return input(prompt)
        except OSError:
            print("입력을 받을 수 없는 환경입니다. 기본값(0) 선택.")
            return "0"

    def show_banner(self):
        banner = """
================================================================================
=========================+--------------------------------+=========================
=========================|         ███████████████       |=========================
=========================|         BLACK ARMOURY         |=========================
=========================|         ███████████████       |=========================
=========================+--------------------------------+=========================
================================================================================
        """
        print(banner)

    def animated_loading_bar(self):
        def loading_animation():
            for frame in itertools.cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷", "⣿", "⠿", "⠾", "⠽", "⠼", "⠻"]):
                if self.loading_done:
                    break
                sys.stdout.write(f"\r로딩 중 {frame} ")
                sys.stdout.flush()
                time.sleep(0.15)

        loader = threading.Thread(target=loading_animation)
        loader.daemon = True
        loader.start()

        time.sleep(3)  # 로딩 시간 조절
        self.loading_done = True
        sys.stdout.write("\r로딩 완료!     \n")
        sys.stdout.flush()

    def show_menu(self):
        self.show_banner()
        self.animated_loading_bar()
        print("\nBLACKY 치트 시트: 모의침투 및 버그바운티")
        while True:
            for key, (desc, _) in self.menu.items():
                print(f"{key}. {desc}")
            choice = self.input_function("선택: ").strip()

            if choice in self.menu:
                self.menu[choice][1]()  # 선택된 함수 실행
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

    def show_bug_bounty(self):
        submenu = {
            "1": ("BURP URL", "웹 트래픽을 인터셉트하고 보안 취약점을 분석하는 도구", "https://portswigger.net/burp"),
            "2": ("POC", "취약점이 실제로 악용될 수 있음을 증명하는 코드", "https://www.exploit-db.com/"),
            "3": ("OWASP10", "가장 중요한 웹 애플리케이션 보안 리스크 TOP 10", "https://owasp.org/www-project-top-ten/")
        }
        self.display_submenu("버그바운티", submenu)

    def show_pentest(self):
        submenu = {
            "1": ("정보수집", "대상 시스템의 정보를 수집하는 과정"),
            "1-1": ("NMAP - MAN", "네트워크 스캐닝 도구로 포트 및 서비스 탐색", "https://nmap.org/book/man.html"),
            "1-2": ("NIKTO - URL + MAN", "웹서버의 보안 취약점을 분석하는 도구", "https://cirt.net/nikto2"),
            "2": ("취약점 분석", "대상 시스템의 보안 취약점을 찾는 과정", "https://owasp.org/www-project-vulnerability-management-guide/"),
            "3": ("익스플로잇", "발견된 취약점을 이용하여 공격을 수행하는 단계", "https://www.exploit-db.com/"),
            "4": ("후속 익스플로잇", "권한 상승, 데이터 탈취 등의 추가 공격 단계", "https://blog.rapid7.com/tag/post-exploitation/"),
            "5": ("피벗팅", "내부 네트워크로 이동하여 추가 공격을 수행하는 기법", "https://pentestlab.blog/2017/03/17/network-pivoting-techniques/")
        }
        self.display_submenu("모의침투 테스트", submenu)

    def show_payloads(self):
        print("\nPAYLOAD 관련 정보 출력\n")

    def show_report_writing(self):
        print("\n보고서 작성 가이드 출력\n")

    def display_submenu(self, title, submenu):
        while True:  # 하위 메뉴 유지
            print(f"\n{title}")
            for key, (desc, explanation, *url) in submenu.items():
                print(f"{key}. {desc}")

            print("0. 뒤로 가기")  # 뒤로 가기 추가
            choice = self.input_function("선택: ").strip()

            if choice == "0":  # 사용자가 뒤로 가기를 선택하면 탈출
                break
            elif choice in submenu:
                desc, explanation, *url = submenu[choice]
                print(f"\n🔹 {desc}")
                print(f"📌 설명: {explanation}")
                if url:
                    print(f"🔗 참고 링크: {url[0]}\n")
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

    def exit_program(self):
        print("프로그램을 종료합니다.")
        exit(0)


if __name__ == "__main__":
    cheat_sheet = BlackyArmoury()
    cheat_sheet.show_menu()
