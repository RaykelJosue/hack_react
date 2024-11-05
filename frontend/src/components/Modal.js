import React from 'react';
import '../index.css';

const Modal = ({ isOpen, onClose, children }) => {
    console.log("Modal isOpen:", isOpen);
    return (
        <div className={`modal-overlay ${isOpen ? 'modal-visible' : ''}`}>
            <div className="modal-container">
                <button className="modal-close" onClick={onClose}>X</button>
                {children}
            </div>
        </div>
    );
};

export default Modal;