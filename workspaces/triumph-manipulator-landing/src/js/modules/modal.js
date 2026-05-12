export function initModal() {
    const openButtons = document.querySelectorAll('[data-modal-open]');
    const closeButtons = document.querySelectorAll('[data-modal-close]');

    const openModal = (id) => {
        const modal = document.getElementById(id);
        if (!modal) return;

        if (modal.getAttribute('aria-hidden') === 'false') return;

        modal.classList.add('is-open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    };

    const closeModal = (modal) => {
        modal.classList.remove('is-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    };

    openButtons.forEach((button) => {
        button.addEventListener('click', () => {
            openModal(button.getAttribute('data-modal-open'));
        });
    });

    closeButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const modal = button.closest('[data-modal]');
            if (modal) {
                closeModal(modal);
            }
        });
    });

    document.addEventListener('keydown', (event) => {
        if (event.key !== 'Escape') {
            return;
        }
        const openedModal = document.querySelector('[data-modal][aria-hidden="false"]');
        if (openedModal) {
            closeModal(openedModal);
        }
    });
}
