document.getElementById("chatSubmit").addEventListener("click", async () => {
  const userMessage = document.getElementById("chatInput").value;

  if (!userMessage.trim()) {
    alert("質問を入力してください。");
    return;
  }

  const chatOutput = document.getElementById("chatOutput");
  chatOutput.value = "AIが回答を生成しています...";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();
    if (data.response) {
      chatOutput.value = data.response; // Display AI response
    } else {
      chatOutput.value = "エラーが発生しました。もう一度お試しください。";
    }
  } catch (error) {
    chatOutput.value = "サーバーに接続できませんでした。もう一度お試しください。";
    console.error("Error:", error);
  }
});

// Clear button functionality
document.getElementById("chatClear").addEventListener("click", () => {
  const chatInput = document.getElementById("chatInput");
  const chatOutput = document.getElementById("chatOutput");

  // Clear both text areas
  chatInput.value = "";
  chatOutput.value = "";
});