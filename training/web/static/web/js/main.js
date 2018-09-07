function setSignInFormToLoadingState(e) {
    const form = e.target;
    const button = form.querySelector('.submit-button');

    button.disabled = true;
    button.textContent = 'Please wait...';
}

function main() {
    const signInForm = document.querySelector('.sign-in-form');

    if (signInForm) {
        signInForm.addEventListener('submit', setSignInFormToLoadingState);
    }
}

document.addEventListener('DOMContentLoaded', main);