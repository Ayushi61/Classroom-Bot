import Login from "./login";
import Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";
Enzyme.configure({ adapter: new Adapter() });
import React, { Component } from "react";
import { MemoryRouter } from "react-router";
import { mount } from "enzyme";

describe("routes using memory router", () => {
  it("should show Login component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/login']}">
        <Login />
      </MemoryRouter>
    );
    expect(component.find(Login)).toHaveLength(1);
  });
});
