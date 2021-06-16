import React from 'react';

function Navbar() {
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="#navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>  
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Why Become a Notary</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Why Us?</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Check Our Courses
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="#">Good</a></li>
                                <li><a class="dropdown-item" href="#">Better</a></li>
                                <li><a class="dropdown-item" href="#">Best</a></li>
                                <li><a class="dropdown-item" href="#">Never Let It Rest!</a></li>
                            </ul>
                        </li>
                        <li>
                            <a class="nav-link" href="#">Let's Talk 1-1</a>
                        </li>                    
                    </ul>
                    <form class="d-flex">
                        <input class="form-control me-2" type="search" placeholder="Search The Site" aria-label="Search"></input>
                        <button class="btn btn-outline-success" type="submit">Search</button>
                    </form>
                </div>
            </a>
        </div>
    </nav>
}