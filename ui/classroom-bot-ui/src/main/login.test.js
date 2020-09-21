import Login from "./login";
import Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import React from "react";
import { MemoryRouter } from "react-router";
import { mount } from "enzyme";

Enzyme.configure({ adapter: new Adapter() });

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
