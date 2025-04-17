/**
 * @Date:  2023-02-28
 * @Language: React.js
 * @Description: App.js- This file is the key component of the frontend. It contains the navigation bar and the main page.
 */

import React from "react";
// import { useState } from "react";
// import axios from "axios";
import { RegExForm } from "./components/RegularExpression/form";
import MainPage from "./components/DefaultPage/Mainpage";
import NavigationBar from "./components/Navbar/Navigationbar";

// @Description: This function returns the key components of the frontend.
function App() {
  return (
    <div className="total-main">
      <NavigationBar />
      <MainPage />
      {/* <RegExForm/> */}
    </div>
  );
}

export default App;
