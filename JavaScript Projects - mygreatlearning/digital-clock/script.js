const app: HTMLElement = document.getElementById("app");

interface State {
    nodes: {
        hours: HTMLElement,
        minutes: HTMLElement,
        seconds: HTMLElement,
    };
    functions: {
        hours: (value: number) => void,
        minutes: (value: number) => void,
        seconds: (value: number) => void,
    };
}

const state: State = {
    nodes: {
        hours: app.querySelector("#time #hours"),
        minutes: app.querySelector("#time #minutes"),
        seconds: app.querySelector("#time #seconds"),
    },
    functions: {
        hours: (value: number): void =>
            (state.nodes.hours.textContent = value.toString()),
        minutes: (value: number): void =>
            (state.nodes.minutes.textContent = value.toString()),
        seconds: (value: number): void =>
            (state.nodes.seconds.textContent = value.toString()),
    },
};

function init(): void {
    setInterval(() => {
        update();
        view();
    }, 1000);
}

interface Model {
    hours: number;
    minutes: number;
    seconds: number;
}

const model: Model = {
    hours: 0,
    minutes: 0,
    seconds: 0,
};

function update(): void {
    const date: Date = new Date();
    const hours: number = date.getHours();
    const minutes: number = date.getMinutes();
    const seconds: number = date.getSeconds();

    model.hours = hours;
    model.minutes = minutes;
    model.seconds = seconds;
}

function view(): void {
    const hours: number = model.hours;
    const minutes: number = model.minutes;
    const seconds: number = model.seconds;

    state.functions.hours(hours);
    state.functions.minutes(minutes);
    state.functions.seconds(seconds);
}

init();
