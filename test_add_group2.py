{
  "id": "40b5954f-899d-4670-afaa-a56d3b694d7e",
  "version": "2.0",
  "name": "add_group",
  "url": "http://localhost",
  "tests": [{
    "id": "e9462da3-0f12-46d7-9e82-f409a35b4403",
    "name": "test_add_new_group",
    "commands": [{
      "id": "7fbe1e6d-ed14-4037-b381-81eb6183ce8d",
      "comment": "",
      "command": "open",
      "target": "/addressbook/",
      "targets": [],
      "value": ""
    }, {
      "id": "3385d0ab-d073-43ce-be92-cda184283090",
      "comment": "",
      "command": "setWindowSize",
      "target": "1936x1056",
      "targets": [],
      "value": ""
    }, {
      "id": "46427bd8-1a37-45eb-ae1e-9de50d5053db",
      "comment": "",
      "command": "click",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e951d348-9d75-4e87-b6ef-4470cb2a7ebe",
      "comment": "",
      "command": "click",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "bd5d21ff-ff1f-45e4-8080-ea02bf6368ab",
      "comment": "",
      "command": "type",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "admin"
    }, {
      "id": "9366b740-bfa3-4d8f-8f77-5834faaee9fa",
      "comment": "",
      "command": "click",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5aaccb0d-e90c-4d15-9480-f597d0e47c26",
      "comment": "",
      "command": "click",
      "target": "css=input:nth-child(7)",
      "targets": [
        ["css=input:nth-child(7)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[3]", "xpath:idRelative"],
        ["xpath=//input[3]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "50ee223a-764d-449c-8d7f-e5828991fc06",
      "comment": "",
      "command": "click",
      "target": "linkText=groups",
      "targets": [
        ["linkText=groups", "linkText"],
        ["css=.admin > a", "css:finder"],
        ["xpath=//a[contains(text(),'groups')]", "xpath:link"],
        ["xpath=//div[@id='nav']/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'group.php')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'groups')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "7d6998cb-59e6-48ef-b6cd-2d20b9df87d3",
      "comment": "",
      "command": "click",
      "target": "name=new",
      "targets": [
        ["name=new", "name"],
        ["css=form:nth-child(2) > input:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='new']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "dc096435-3640-4b56-94eb-518bc38e20f5",
      "comment": "",
      "command": "click",
      "target": "css=label:nth-child(1)",
      "targets": [
        ["css=label:nth-child(1)", "css:finder"],
        ["xpath=//div[@id='content']/form/label", "xpath:idRelative"],
        ["xpath=//label", "xpath:position"],
        ["xpath=//label[contains(.,'Group name:')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b0ff9ade-da3c-4f9b-bc2b-cadf5a3c5e7b",
      "comment": "",
      "command": "click",
      "target": "name=group_name",
      "targets": [
        ["name=group_name", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='group_name']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4e14066c-b564-4fe2-b15d-967b4d61a541",
      "comment": "",
      "command": "type",
      "target": "name=group_name",
      "targets": [
        ["name=group_name", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='group_name']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": "hdh"
    }, {
      "id": "ba5b8272-6d58-457a-a2de-f76a35ad6e47",
      "comment": "",
      "command": "click",
      "target": "name=group_header",
      "targets": [
        ["name=group_header", "name"],
        ["css=textarea:nth-child(5)", "css:finder"],
        ["xpath=//textarea[@name='group_header']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea", "xpath:idRelative"],
        ["xpath=//textarea", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "bd5816c4-f11b-49dd-b6d4-5eb9e9808fe9",
      "comment": "",
      "command": "type",
      "target": "name=group_header",
      "targets": [
        ["name=group_header", "name"],
        ["css=textarea:nth-child(5)", "css:finder"],
        ["xpath=//textarea[@name='group_header']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea", "xpath:idRelative"],
        ["xpath=//textarea", "xpath:position"]
      ],
      "value": "dgfdfhb"
    }, {
      "id": "61565c10-fd3d-4d1a-96b7-6738cd90f713",
      "comment": "",
      "command": "click",
      "target": "css=form:nth-child(2)",
      "targets": [
        ["css=form:nth-child(2)", "css:finder"],
        ["xpath=//form[@action='/addressbook/group.php']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form", "xpath:idRelative"],
        ["xpath=//div[4]/form", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e43edf32-7734-4739-811c-596ddf70fab9",
      "comment": "",
      "command": "click",
      "target": "name=group_footer",
      "targets": [
        ["name=group_footer", "name"],
        ["css=textarea:nth-child(8)", "css:finder"],
        ["xpath=//textarea[@name='group_footer']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea[2]", "xpath:idRelative"],
        ["xpath=//textarea[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "24a9cba2-5d29-4e99-9534-700dfb7f1ca6",
      "comment": "",
      "command": "type",
      "target": "name=group_footer",
      "targets": [
        ["name=group_footer", "name"],
        ["css=textarea:nth-child(8)", "css:finder"],
        ["xpath=//textarea[@name='group_footer']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea[2]", "xpath:idRelative"],
        ["xpath=//textarea[2]", "xpath:position"]
      ],
      "value": "dgdstg"
    }, {
      "id": "3e69d5a7-0dd9-49ab-bf32-92a4a71cb7ea",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(11)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "558b2bb3-16d0-4a61-8797-149de94cc7e8",
      "comment": "",
      "command": "click",
      "target": "linkText=groups",
      "targets": [
        ["linkText=groups", "linkText"],
        ["css=.admin > a", "css:finder"],
        ["xpath=//a[contains(text(),'groups')]", "xpath:link"],
        ["xpath=//div[@id='nav']/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'group.php')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'groups')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "f34d0501-4dc3-4370-8ddc-9128095ea41b",
      "comment": "",
      "command": "click",
      "target": "linkText=Logout",
      "targets": [
        ["linkText=Logout", "linkText"],
        ["css=a:nth-child(3)", "css:finder"],
        ["xpath=//a[contains(text(),'Logout')]", "xpath:link"],
        ["xpath=//a[@onclick='document.logout.submit();']", "xpath:attributes"],
        ["xpath=//div[@id='top']/form/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '#')]", "xpath:href"],
        ["xpath=//a", "xpath:position"],
        ["xpath=//a[contains(.,'Logout')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b75c503f-6627-4c1c-9bd8-a6f04619ca19",
      "comment": "",
      "command": "type",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "admin"
    }]
  }],
  "suites": [{
    "id": "34be34b8-fef5-4242-aacc-e168c9fd875d",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["e9462da3-0f12-46d7-9e82-f409a35b4403"]
  }],
  "urls": ["http://localhost/"],
  "plugins": []
}