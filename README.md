# CameraProject
카메라 프로젝트

2020 0817 석근
렌즈/바디 별  별점 평균을 내림차순 정렬하여 가져와서 출력하는 데에는 성공했지만
1위 2위 3위 이렇게 인덱스 증가하면서 어떻게 출력해줄지 모르겠습니다,, 검색해봤는데 {{ forloop.counter }} 쓰면 된다는데 안돼요

2020 0818 석근
한민형 상준형과 고민끝에 모델을 갈기로 결정, lenstype bodytype 모델은 더이상 사용하지않고 Type으로 바디/렌즈로만
나눠주기로 함. views들을  고쳐야함. 참고로 외래키이므로 Product에서 타입을 결정할 땐 pdtype_id = 1  or  2  로 사용하기바람. (1 :바디 ,2 : 렌즈)