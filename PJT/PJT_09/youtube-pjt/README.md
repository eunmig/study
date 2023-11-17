# 09-PJT 정휘원 박은미

## 예상 일정표

|시간|목표|중요도|예상 난이도|
|:---|---------:|:---:|:---:|
|11:00~12:00|수업내용 정리/바로 적용가능한 과제 확인|★★★★| ? |
|13:00~14:00|과제 A 해결 (은미, 휘원)|★★★|★★★|
|14:00~15:00|과제 B 해결 (은미) / 과제 C 해결 (휘원)|★★|★★|
|15:00~15:30|구현 된 부분 확인, 상호 코드 리뷰|★★|★★|
|15:30~16:30|과제 D 도전|★★★|★★|
|16:30~17:00|README 작성|★|★★★★|


<div style="text-align: right">중요도</div>


<div style="text-align: right">|아주높음|높음|보통|낮음|</div>
<div style="text-align: right"></div>
<div style="text-align: right">|★★★★|★★★|★★|★|</div>

## 실제 진행상황
 |시간|진행|
 |---|---|
 |11:00~12:00| 프로젝트 예상 일정표 작성|
 |13:00~14:30| 은미/휘원 - 과제 A 구현|
 |14:30~16:00| 은미 - 과제 C 구현|
 |           | 휘원 - 과제 B 구현| 
 |16:00~16:40| 휘원 - 과제 C 디버깅|
 |16:40~17:00| 은미/휘원 - README 작성|

 ## 느낀점 
 ### 1. problem A
 A : 동영상 검색결과 출력
YouTube API를 사용하여 비디오를 검색하는게 목표

```
// 비디오 검색을 수행하는 함수
const searchVideo = function(keyword) {
    const url = 'https://www.googleapis.com/youtube/v3/search'
    const params = {
        key,
        part: 'snippet',
        q: keyword,
        type: 'video'
    }
    axios({
        method: 'get',
        url,
        params,
    })
        .then(res=>{
            videos.value = res.data.items
            // saveData(videos.value)
        })
        .catch(err => {

        })
}   
```

### 2. problem B
B : 동영상 상세 정보 출력

1. 최초 시도 -> VideoCard 라는 컴포넌트를 클릭하면(썸네일) detail 페이지로 이동하며 param 과 query로 데이터를 전송 ->
    특정 데이터만 넘어가며 필요한 데이터가 더 생길때마다 계속 추가 해줘야 하고, 잦은 에러가 일어남

2. 다음 시도 -> 검색 결과의 특정 url(e.g - adele-hello)라고 했을 때, 해당 페이지에 대하여 다시 api에서 데이터를 요청할 수 있는지 확인 
능력 밖

3. 마지막 시도 -> 구조적으로 for 문을 사용하여 검색 시 생성되는 동영상들은 개념적으로 각각 다른 jsonData를 갖고 있는 객체라고 생각.
jsonData 전체를 그렇다면 detail 페이지로 넘기는 방법 구현
(이는 과제 C 디버깅을 하며 다시 필요해짐.)


### 3. problem C
  C : 나중에 볼 동영상 저장 및 삭제

  Local Storage를 활용하여 동영상 저장

  ```
  const addVideo = (video) => {
  // 현재 localStorage에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingVideos = JSON.parse(localStorage.getItem('youtube-videos')) || []

  // 중복된 데이터가 있는지 확인
  const isDuplicate = existingVideos.length > 0 && existingVideos.find((item) => item.id === video.id)

  // 중복이 아니라면 추가
  if (!isDuplicate) {
    alert('나중에 볼 동영상에 추가합니다');
    existingVideos.push(video);
  } else {
    alert('이미 있는 동영상입니다. 나중에 볼 동영상으로 이동합니다.')
  }

  // 수정된 데이터를 localStorage에 저장
  localStorage.setItem('youtube-videos', JSON.stringify(existingVideos))

  // 이동할 페이지 또는 추가적인 동작을 수행하려면 여기에서 처리
};
  ```

과제 C 디버깅(휘원)

- 동영상 추가 시, 검색했던 리스트 전체가 계속 추가됨.
- 검색시 localStorage에 save 한 배열의 이름이, 추가하는 배열의 이름과 같음 -> 검색시 모든 리스트가 계속 저장이 되는것.
- 이를 해결하기 위해 다시 과제 B부터 전체 변경을 이어나감

## 느낀점

*휘원*

    생각보다 어려운 난이도에 중간에 멘탈을 놓쳤었다.
    시간 내에 도전과제까지 할 수 있을 줄 알았는데 해결하지 못했다.

    시작 전에 어떤 방식으로 과제를 진행할지 계획을 세울 때
    각 과제 간 어떤 방식으로 데이터가 연결되어 있는지 보고, 전체 구조를 먼저 짜는 것이 필요하다고 느꼈다.

*은미 *

    problem C 구현하면서 동영상을 추가하는 동작을 수행하면 검색한 동영상 전체가 나중에 볼 동영상 목록에 추가되는 에러가 생겼다.

    파트너가 원하는 동영상만 추가될 수 있게 디버깅하였다. 

## 실패 과제 D
