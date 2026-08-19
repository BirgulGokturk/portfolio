/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./index.html'],
    darkMode: 'class',
    theme: {
        extend: {
            fontFamily: {
                display: ['"Poppins"', 'system-ui', '-apple-system', '"Segoe UI"', 'sans-serif'],
                sans: ['"Poppins"', 'system-ui', '-apple-system', '"Segoe UI"', 'sans-serif'],
            },
            colors: {
                cream: 'var(--color-cream)',
                sand: 'var(--color-sand)',
                taupe: 'var(--color-taupe)',
                muted: 'var(--color-muted)',
                ink: 'var(--color-ink)',
                accent: 'var(--color-accent)',
                accentLight: 'var(--color-accent-light)',
            },
            animation: {
                'fade-up': 'fadeUp 0.7s ease forwards',
                'fade-in': 'fadeIn 0.6s ease forwards',
            },
            keyframes: {
                fadeUp: {
                    '0%': { opacity: '0', transform: 'translateY(24px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' },
                },
            },
        },
    },
    plugins: [],
};
