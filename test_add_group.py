{
  "id": "760f9d7a-cf2c-4d87-880b-040603219a3c",
  "version": "2.0",
  "name": "add_group",
  "url": "http://localhost",
  "tests": [{
    "id": "c14e02e2-71f9-432f-93be-bb74b4a63e85",
    "name": "Untitled",
    "commands": [{
      "id": "5a80edcd-cc3b-4268-a16c-d959a30d82ea",
      "comment": "",
      "command": "open",
      "target": "/addressbook/",
      "targets": [],
      "value": ""
    }, {
      "id": "ff0a0419-d21e-4d8c-8083-8866f4fbdef4",
      "comment": "",
      "command": "setWindowSize",
      "target": "995x680",
      "targets": [],
      "value": ""
    }, {
      "id": "bee0a229-8a1d-4475-866d-da8c4c98a62d",
      "comment": "",
      "command": "click",
      "target": "id=LoginForm",
      "targets": [
        ["id=LoginForm", "id"],
        ["name=LoginForm", "name"],
        ["css=#LoginForm", "css:finder"],
        ["xpath=//form[@id='LoginForm']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form", "xpath:idRelative"],
        ["xpath=//form", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c5cbb6eb-4692-4ce7-856e-13143505fd68",
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
      "id": "d97612ef-f2c7-474b-932a-9ff32df7c6a3",
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
      "id": "6a72bbab-09e7-4630-a671-6d837caa22a3",
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
      "id": "4f53e8d2-b8f8-4058-8364-1928f048008d",
      "comment": "",
      "command": "type",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": "secret"
    }, {
      "id": "ebbb7f23-76c3-4a0f-8923-0a3f28d93d7b",
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
      "id": "9d7a4d65-1071-4b29-8146-0f5a65356902",
      "comment": "",
      "command": "click",
      "target": "id=container",
      "targets": [
        ["id=container", "id"],
        ["css=#container", "css:finder"],
        ["xpath=//div[@id='container']", "xpath:attributes"],
        ["xpath=//div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "55161f44-dd89-450c-bbb8-5c2cdd41d007",
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
      "id": "4cf68f02-e358-4633-bfc3-2245a1608930",
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
      "id": "d28ddf70-fb90-41da-9c38-c9e029d18abc",
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
      "id": "8ef9328d-3c2a-427a-b08a-e467530c37fd",
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
      "id": "7d69bda9-af5c-4629-9cfe-98af230970a1",
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
      "value": "hjfgjf"
    }, {
      "id": "1cda6d5d-f0b7-4d76-98f2-07d6a45bcb8a",
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
      "id": "992a16ce-5156-4ca8-bf28-682f56125409",
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
      "value": "nbfvn"
    }, {
      "id": "dfd6d43e-22c4-4180-ab0b-80e8710fc446",
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
      "id": "f34b35ca-309b-4878-a0b8-e5ce2ed50900",
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
      "value": "fngnfg"
    }, {
      "id": "3ed770b0-23bc-4e27-99f9-efea6540068e",
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
      "id": "519ee5ea-af96-4073-bffb-a47ad506c8bd",
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
      "id": "1327f07d-004a-4af5-a03b-97878f0b7a99",
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
      "id": "614e940f-e357-4903-b86b-e529218afaa2",
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
      "id": "d5262243-aea5-4395-b3df-70679a1a30fc",
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
      "id": "20b503d6-2514-436f-b7bf-ca6b0c892062",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9dbc3a75-9fc3-47dd-9d7e-6314487ff1f4",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e143218b-690d-44b1-851d-ba69699eaf60",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "01e95c51-1d02-4fed-9e30-3cfabe935b22",
      "comment": "",
      "command": "doubleClick",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ca528ac0-c094-4ff7-9eb6-9f7b4fab5823",
      "comment": "",
      "command": "click",
      "target": "id=content",
      "targets": [
        ["id=content", "id"],
        ["css=#content", "css:finder"],
        ["xpath=//div[@id='content']", "xpath:attributes"],
        ["xpath=//div[@id='container']/div[4]", "xpath:idRelative"],
        ["xpath=//div[4]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "3e03a036-8b49-4c02-a3fe-b3d2ebb9d895",
      "comment": "",
      "command": "click",
      "target": "css=html",
      "targets": [
        ["css=html", "css:finder"],
        ["xpath=//html", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "161915f5-4b4a-4334-9a10-415a6b4b275e",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["c14e02e2-71f9-432f-93be-bb74b4a63e85"]
  }],
  "urls": ["http://localhost/"],
  "plugins": []
}