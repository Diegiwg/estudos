const app = document.getElementById("app");

function pickRandom(array) {
    console.log(array, array[Math.floor(Math.random() * array.length)]);
    return array[Math.floor(Math.random() * array.length)];
}

async function loadData() {
    const source = await fetch("questions.json");
    const questions = await source.json();
    return questions;
}

const questions = (async function () {
    const data = await loadData();
    return data;
})();

console.log(questions);

let model = {
    pergunta: "",
    resposta: "",
    alternativas: "",

    perguntas: await questions,
};

function update() {
    const data = pickRandom(model.perguntas);
    if (!data) return;

    model.pergunta = data.pergunta;
    model.resposta = data.resposta;
    model.alternativas = data.alternativas;
}

function view() {
    update();
    const { pergunta, alternativas } = model;

    console.log(model);
    console.log(pergunta, alternativas);

    app.querySelector("#A").textContent = alternativas[0];
    app.querySelector("#B").textContent = alternativas[1];
    app.querySelector("#C").textContent = alternativas[2];
    app.querySelector("#D").textContent = alternativas[3];
    app.querySelector("#E").textContent = alternativas[4];

    app.querySelector("#question-string").textContent = pergunta;
}

loadData();

(function init() {
    update();
    view();
})();
