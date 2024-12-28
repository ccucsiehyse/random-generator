<template>
  <div id="app">
    <h1>隨機數字產生器</h1>
    <button @click="fetchRandomNumber">獲取隨機數字</button>
    <p v-if="randomNumber !== null">後端回傳的隨機數字：{{ randomNumber }}</p>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const randomNumber = ref(null); // 儲存後端回傳的數字
    const errorMessage = ref(''); // 儲存錯誤訊息

    // 使用 Fetch API 發送請求至後端
    const fetchRandomNumber = async () => {
      try {
	  const response = await fetch('http://localhost:8000/api/random');
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        const data = await response.json(); // 解析 JSON 格式的回應
        randomNumber.value = data.randomNumber; // 假設後端返回的 key 是 'randomNumber'
        errorMessage.value = ''; // 清除之前的錯誤訊息
      } catch (error) {
        errorMessage.value = '獲取數據時發生錯誤: ' + error.message;
        console.error('Fetch error:', error);
      }
    };

    return {
      randomNumber,
      fetchRandomNumber,
      errorMessage
    };
  }
};
</script>

<style scoped>
#app {
  text-align: center;
  margin-top: 50px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

p {
  margin-top: 20px;
  font-size: 18px;
  color: #333;
}
</style>

