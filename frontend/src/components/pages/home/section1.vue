<script>

</script>

<template>
    <section>
        <!--Logo -->
        <header id="header" class="sticky-header">
            <div class="logo-container">
                <img src="/homepagelogo.png" alt="STOCKFA Logo" class="logo" />
            </div>
        </header>

        <!-- GitHub Button -->
        <a href="https://github.com/nishanth964/stockFA" target="_blank" rel="noopener noreferrer" class="btn-github">
            <svg width="24" height="24" viewBox="0 0 16 16" fill="none">
                <path
                    d="M7.99992 1.33331C7.12444 1.33331 6.25753 1.50575 5.4487 1.84078C4.63986 2.17581 3.90493 2.66688 3.28587 3.28593C2.03563 4.53618 1.33325 6.23187 1.33325 7.99998C1.33325 10.9466 3.24659 13.4466 5.89325 14.3333C6.22659 14.3866 6.33325 14.18 6.33325 14C6.33325 13.8466 6.33325 13.4266 6.33325 12.8733C4.48659 13.2733 4.09325 11.98 4.09325 11.98C3.78659 11.2066 3.35325 11 3.35325 11C2.74659 10.5866 3.39992 10.6 3.39992 10.6C4.06659 10.6466 4.41992 11.2866 4.41992 11.2866C4.99992 12.3 5.97992 12 6.35992 11.84C6.41992 11.4066 6.59325 11.1133 6.77992 10.9466C5.29992 10.78 3.74659 10.2066 3.74659 7.66665C3.74659 6.92665 3.99992 6.33331 4.43325 5.85998C4.36659 5.69331 4.13325 4.99998 4.49992 4.09998C4.49992 4.09998 5.05992 3.91998 6.33325 4.77998C6.85992 4.63331 7.43325 4.55998 7.99992 4.55998C8.56659 4.55998 9.13992 4.63331 9.66659 4.77998C10.9399 3.91998 11.4999 4.09998 11.4999 4.09998C11.8666 4.99998 11.6333 5.69331 11.5666 5.85998C11.9999 6.33331 12.2533 6.92665 12.2533 7.66665C12.2533 10.2133 10.6933 10.7733 9.20659 10.94C9.44659 11.1466 9.66659 11.5533 9.66659 12.1733C9.66659 13.0666 9.66659 13.7866 9.66659 14C9.66659 14.18 9.77325 14.3933 10.1133 14.3333C12.7599 13.44 14.6666 10.9466 14.6666 7.99998C14.6666 7.1245 14.4941 6.25759 14.1591 5.44876C13.8241 4.63992 13.333 3.90499 12.714 3.28593C12.0949 2.66688 11.36 2.17581 10.5511 1.84078C9.7423 1.50575 8.8754 1.33331 7.99992 1.33331V1.33331Z"
                    fill="currentcolor"></path>
            </svg>
            <span>View on Github</span>
        </a>

        <!-- Dark Theme Button -->
        <div class="dark-theme-toggle">
            <input id="darkmode-toggle" type="checkbox" />
            <label for="darkmode-toggle">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="sun">
                    <g transform="translate(0 512) scale(.1 -.1)">
                        <path
                            d="m2513 5105c-59-25-63-46-63-320 0-266 4-288 54-315 33-17 79-17 112 0 50 27 54 49 54 315 0 275-4 295-65 321-42 17-51 17-92-1z">
                        </path>
                        <path
                            d="m754 4366c-28-28-34-41-34-77 0-42 3-45 188-231l187-188h47c39 0 52 5 77 31 26 25 31 38 31 77v47l-188 187c-186 185-189 188-231 188-36 0-49-6-77-34z">
                        </path>
                        <path
                            d="m4058 4212-188-187v-47c0-39 5-52 31-77 25-26 38-31 77-31h46l188 188c186 186 188 188 188 231 0 36-6 49-34 77s-41 34-77 34c-42 0-45-3-231-188z">
                        </path>
                        <path
                            d="m2440 4224c-453-50-760-192-1056-488-264-264-419-570-475-936-17-109-17-371 0-480 56-366 211-672 475-936s570-419 936-475c109-17 371-17 480 0 366 56 672 211 936 475 225 225 358 455 438 758 38 143 50 249 50 418 0 219-30 388-104 590-137 372-450 719-813 901-143 72-315 128-474 154-89 15-329 26-393 19zm335-235c305-46 582-186 805-409 567-567 567-1473 0-2040s-1473-567-2040 0-567 1473 0 2040c328 328 777 476 1235 409z">
                        </path>
                        <path
                            d="m54 2651c-20-12-37-34-44-55-16-49 2-101 44-127 28-17 52-19 279-19 268 0 289 4 317 54 17 33 17 79 0 112-28 50-49 54-317 54-227 0-251-2-279-19z">
                        </path>
                        <path
                            d="m4512 2657c-73-41-73-155 0-193 21-11 81-14 275-14 227 0 251 2 279 19 42 26 60 78 44 127-7 21-24 43-44 55-28 17-52 19-281 19-181-1-256-4-273-13z">
                        </path>
                        <path
                            d="m908 1062c-185-186-188-189-188-231 0-36 6-49 34-77s41-34 77-34c43 0 45 2 231 188l188 188v46c0 39-5 52-31 77-25 26-38 31-77 31h-47l-187-188z">
                        </path>
                        <path
                            d="m3901 1219c-26-25-31-38-31-77v-47l188-187c186-185 189-188 231-188 36 0 49 6 77 34s34 41 34 77c0 43-2 45-188 231l-188 188h-46c-39 0-52-5-77-31z">
                        </path>
                        <path
                            d="m2540 663c-87-28-90-37-90-330 0-227 2-251 19-279 40-66 142-66 182 0 17 28 19 52 19 279 0 266-4 291-52 314-32 16-60 22-78 16z">
                        </path>
                    </g>
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="moon">
                    <g transform="translate(0 512) scale(.1 -.1)">
                        <path
                            d="m2090 5105c-248-51-443-118-659-226-514-256-909-652-1161-1163-94-191-139-311-185-490-127-500-110-999 51-1468 133-389 331-706 624-998 403-404 875-642 1460-736 147-24 529-24 693 0 539 78 981 283 1390 644 362 319 647 793 766 1270 46 186 56 256 42 299-22 71-80 116-151 117-73 1-104-19-181-116-307-390-733-627-1233-689-119-14-385-7-501 15-582 106-1066 469-1321 991-120 246-171 452-181 731-21 586 230 1126 695 1493 96 75 117 107 117 177 0 85-67 155-153 160-26 1-76-3-112-11zm110-149c0-2-26-23-57-47-81-60-254-230-325-318-213-264-353-573-415-916-22-126-25-508-5-625 62-346 195-651 395-910 72-93 228-250 327-329 266-213 571-349 930-413 117-20 499-17 625 5 343 62 652 202 916 415 88 71 258 244 318 325 24 32 46 56 48 54s-8-60-23-128c-127-606-501-1155-1027-1505-780-521-1798-535-2602-36-295 183-594 482-777 777-335 539-445 1180-308 1795 138 621 515 1158 1060 1511 136 88 374 201 530 253 148 49 390 106 390 92z">
                        </path>
                    </g>
                </svg>
            </label>
        </div>
    </section>
</template>

<style scoped>

.sticky-header {
    position: sticky;
    top: 0;
    width: 100%;
    height: 300px;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.logo {
    height: 500px;
    filter: drop-shadow(0 5px 4px rgba(0, 0, 0, 0.5));
}

/* GitHub Button */
.btn-github {
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 1000;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    font-size: 0.825rem;
    font-weight: 800;
    color: #ffffff;
    background-color: rgba(0, 0, 0, 0.4);
    border-radius: 100px;
    box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.04), inset 0 0 0 1px rgba(255, 255, 255, 0.04);
    transition: all 0.3s ease;
}

.btn-github:hover {
    background-color: rgba(0, 0, 0, 0.5);
    box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.08), inset 0 0 0 1px rgba(252, 232, 3, 0.08);
    transform: translateY(-0.25rem);
}

/* Dark Theme Toggle */
.dark-theme-toggle {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
}

.dark-theme-toggle input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
}

.dark-theme-toggle label {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 46px;
    height: 46px;
    background: rgb(246, 244, 244);
    border: 1px solid #ffffff;
    border-radius: 10px;
    cursor: pointer;
    position: relative;
    transition: all 0.5s;
}

.dark-theme-toggle label:active {
    border-radius: 5px;
}

.dark-theme-toggle label svg {
    position: absolute;
    width: 20px;
    transition: opacity 0.3s;
    z-index: 1;
}

.dark-theme-toggle label .moon {
    fill: #000;
    opacity: 1;
}

.dark-theme-toggle label .sun {
    width: 24px;
    fill: #fff;
    opacity: 0;
}

.dark-theme-toggle input:checked+label {
    background: #4a6cf7;
}

.dark-theme-toggle input:checked+label .moon {
    opacity: 0;
}

.dark-theme-toggle input:checked+label .sun {
    opacity: 1;
}

.dark-theme-toggle input:checked~.content {
    background-color: #16174b;
}
</style>