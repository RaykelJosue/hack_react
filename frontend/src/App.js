import React, { useState } from 'react';
import UserList from './components/UserList';
import './index.css';

const App = () => {
    const [darkMode, setDarkMode] = useState(false);

    const toggleDarkMode = () => {
        setDarkMode(!darkMode);
    };

    return (
        <div className={`app ${darkMode ? 'dark' : ''}`}>
            <button 
                className="dark-mode-toggle" 
                onClick={toggleDarkMode}
            >
                {darkMode ? '☀️' : '🌙'}
            </button>
            <UserList />
        </div>
    );
};

export default App;