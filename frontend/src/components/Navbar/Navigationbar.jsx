import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import "./Navigationbar.css";

export default function NavigationBar() {
  const navRef = useRef();

  const showNavbar = () => {
    navRef.current.classList.toggle("responsive_nav");
  };

  return (
    <header>
      {/* <img
                alt="logo"
                width="120"
                height="40"
                className="nav-logo"
            /> */}

      <nav ref={navRef}>
        <a href="/#">
          {" "}
          <h4>Sniffs CSV</h4>{" "}
        </a>
        <div class="topnav-right">
          <a href="/#">HELP</a>
          <a href="/#">ABOUT US</a>
        </div>
        <button className="nav-btn nav-close-btn" onClick={showNavbar}>
          <FaTimes />
        </button>
      </nav>
      <button className="nav-btn" onClick={showNavbar}>
        <FaBars />
      </button>
    </header>
  );
}
