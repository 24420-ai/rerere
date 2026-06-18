# [신규 추가] 채널 기본 정보 안내 - 방송규칙 처리 라우트
@app.route("/channel-rules", methods=["POST"])
def channel_rules_skill():
    data = request.get_json(silent=True) or {}
    
    # 카카오톡 챗봇 설정 창에서 지정한 파라미터명을 가져옵니다.
    # 여기서는 파라미터 이름을 'rule_type'으로 가정했습니다.
    params = data.get("action", {}).get("params", {})
    rule_type = params.get("rule_type", "기본").strip()

    # 파라미터 조건에 따른 방송 규칙 분기 처리
    if "이벤트" in rule_type:
        rules_text = (
            "🎉 [이벤트 진행 시 방송 규칙]\n\n"
            "1. 중복 참여 및 부적절한 방법 참여 시 제외됩니다.\n"
            "2. 당첨자 비방이나 결과 불복성 도배는 제재 대상입니다.\n"
            "3. 모두가 즐거운 이벤트를 위해 매너를 지켜주세요!"
        )
    else:
        # 기본 방송 규칙 (파라미터가 없거나 '기본'일 때)
        rules_text = (
            "📺 [기본 방송 규칙 안내]\n\n"
            "1. 욕설, 비하 발언 및 정치적 발언은 절대 금지합니다.\n"
            "2. 타 스트리머/크리에이터 언급 및 비교를 자제해 주세요.\n"
            "3. 시청자 간의 과도한 친목(닉네임 부르기 등)은 금합니다.\n"
            "4. 클린한 방송 환경을 위해 매너 채팅 부탁드립니다! 🙏"
        )

    # 선생님이 만들어두신 kakao_text 함수를 그대로 활용하여 응답
    return jsonify(kakao_text(rules_text))
