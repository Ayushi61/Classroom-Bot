import React from "react";
import {
  render,
  screen,
} from "@testing-library/react";
//import ReactDOM from "react-dom";
import App from "./App";
import TopBar from "./common/topBar";
//import Body from "./common/body";

test("renders code flow", async () => {
  const { debug } = render(<App />);
  debug();
});
test("renders home page", async () => {
  // const { getByText } = render(<App />);
  // getByText("Graph 1");
});

test("render topbar", () => {
  render(<TopBar />);
  expect(screen.getByText(/Classroom Slack Bot - Admin/)).toBeInTheDocument();
});

// const links = [
//   { text: "Classroom Slack Bot - Admin", location: "/" },
//   //{ text: "Commands", location: "/commands" },
//   { text: "Data Configuration", location: "/table/datasource" },
// ];


//test("render body", () => {
//render(<Body />);
//expect(screen.getByText(/Classroom Slack Bot - Admin/)).toBeInTheDocument();
//});
