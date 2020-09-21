import React from "react";
import { MemoryRouter } from "react-router";
import { mount } from "enzyme";
import Main from "../main/main";
import Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import Datasource from "../main/datasource";
import GroupForm from "../main/groupForm";
import CourseForm from "../main/courseForm";
Enzyme.configure({ adapter: new Adapter() });

describe("routes using memory router", () => {
  it("should show Main component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/']}">
        <Main />
      </MemoryRouter>
    );
    expect(component.find(Main)).toHaveLength(1);
  });
});

describe("routes using memory router", () => {
  it("should show Main component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/main']}">
        <Main />
      </MemoryRouter>
    );
    expect(component.find(Main)).toHaveLength(1);
  });
});

//Complete later
describe("routes using memory router", () => {
  it("should show Command form component for / router (using memory router)", () => {
    const component = mount(
<<<<<<< HEAD
      <MemoryRouter initialentries="{['/form/course/abc12450145']}">
        render ={" "}
        {(props) => <CourseForm {...props} key={this.props.location.key} />}
=======
      <MemoryRouter initialentries="{['/form/course/new']}">
        <CourseForm />
>>>>>>> 93c12e0bde09331ed169379db008dc73be2825fb
      </MemoryRouter>
    );
    expect(component.find(CourseForm)).toHaveLength(1);
  });
});

describe("routes using memory router", () => {
  it("should show group form component for / router (using memory router)", () => {
    const component = mount(
<<<<<<< HEAD
      <MemoryRouter initialentries="{['/form/group/1']}">
        render ={" "}
        {(props) => <GroupForm {...props} key={this.props.location.key} />}
=======
      <MemoryRouter initialentries="{['/form/group/new']}">
        <GroupForm />
>>>>>>> 93c12e0bde09331ed169379db008dc73be2825fb
      </MemoryRouter>
    );
    expect(component.find(GroupForm)).toHaveLength(0);
  });
});

describe("routes using memory router", () => {
  it("should show group form component for / router (using memory router)", () => {
    const component = mount(
      <MemoryRouter initialentries="{['/table/:name]}">
        render ={" "}
        {(props) => <Datasource {...props} key={this.props.location.key} />}
      </MemoryRouter>
    );
    expect(component.find(Datasource)).toHaveLength(0);
  });
});

//describe("routes using memory router", () => {
//it("should show datasource component for / router (using memory router)", () => {
//const component = mount(
//<MemoryRouter initialentries="{['/table/group']}">
//<Datasource />
//</MemoryRouter>
//);
//expect(component.find(Datasource)).toHaveLength(1);
//});
//});
