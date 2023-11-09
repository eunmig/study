<template>
    <div class="main-page">
        <h2 class="page-title">퀴즈 앱 사용 방법</h2>
        <div class="usage-section">
            <div class="usage-item">
                <h1>1. 퀴즈 목록 확인하기</h1>
                <p class="description">퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요.</p>
                <img src="../assets/quizList.png" alt="quizList" class="screenshot">
            </div>
            <div class="usage-item">
                <h1>2. 퀴즈 생성하기</h1>
                <p class="description">퀴즈는 직접 생성 할수도 있어요</p>
                <img src="../assets/quizCreate.png" alt="quizCreate" class="screenshot">
            </div>
            <div class="usage-item">
                <h1>3. 정답 페이지</h1>
                <p class="description">작성한 답안이 정답인지 확인하세요</p>
                <img src="../assets/quizAnswer.png" alt="quizAnswer" class="screenshot">
            </div>
        </div>
    </div>
</template>
  
  <script setup>
  
  </script>
  

  <style scoped>
  .main-page {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .page-title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .usage-section {
    display: flex;
    flex-direction: column;
  }
  
  .usage-item {
    margin-bottom: 20px;
  }
  
  .screenshot {
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .description {
    font-size: 16px;
    margin-top: 10px;
  }
  </style>