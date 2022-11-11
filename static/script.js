var feedback = document.getElementById("feedback")
if (feedback.textContent == '') {
    document.querySelector("h1").focus()
} else {
    let stringSearch = feedback.textContent.search('not')
    console.log(stringSearch)
    if (stringSearch > 0) {
        feedback.style.color = 'lightgreen';
        stringSearch = 0
    } else { feedback.style.color = 'red'; }
    setTimeout(clear, 10000)
    feedback.focus()
}

function clear() {
    feedback.textContent = '';
}