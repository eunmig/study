axios.(a)('https://api.example.com/data')
	.(b)(function (response) {
	console.log((c))
})


// (a) : get				# 요청메서드 지정
// (b) : then 				# 요청이 성공했을 때 실행할 콜백 함수 지정
// (c) : response.data 		# 응답 데이터 출력