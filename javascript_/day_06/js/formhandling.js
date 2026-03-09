// 가격 number화 하여 배열에 저장
const prices_arr = [];
document.querySelectorAll(".price").forEach(e => {
  prices_arr.push(Number(e.textContent.replace(/,|원/g, "")));
});

// Handler
function updateAll() {
  const rowNum = prices_arr.length - 1; // 행 갯수
  let totalCnt = 0; // 총 수량
  let totalPrice = 0; // 총 합계

  for (let i = 0; i < rowNum; i++) {
    // id 속성 템플릿 리터럴
    const bookId = `book${i+1}`;

    // 요소 -> 객체
    const inputEl = document.getElementById(bookId);
    const rowTotalEl = document.getElementById(bookId+"Total");

    // 수량
    const v = inputEl.value.trim();
    if (!/^\d+$/.test(v)) {
      inputEl.value = "0";
    } else {
      inputEl.value = v;
    }

    const inputData = Number(inputEl.value);
    
    // 책 별 합계
    const price = prices_arr[i];
    const rowTotal = price * inputData;
    rowTotalEl.value = rowTotal.toLocaleString();
    
    // 총 합계 누적
    totalCnt += inputData;
    totalPrice += rowTotal;
  }
  document.getElementById("totalNumber").value = totalCnt.toLocaleString();
  document.getElementById("totalPrice").value = totalPrice.toLocaleString();
}

// Listener
document.querySelector("form").addEventListener("input", updateAll);
