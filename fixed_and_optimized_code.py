user = {
    "user": {
        "name": "Артем",
        "surname": "Багдасарян",
        "memberships": {
            "membership1": {
                "project": {
                    "id": 123,
                    "name": "project1"
                },
                "roles": {
                    "name": "Не участвует",
                    "name": "Заказчик"
                }
            },
            "membership2": {
                "project": {
                    "id": 456,
                    "name": "project2"
                },
                "roles": {
                    "name": "Участник"
                }
            },
            "membership3": {
                "project": {
                    "id": 789,
                    "name": "someproject1"
                },
                "roles": {
                    "name": "Не участвует",
                    "name": "Заказчик"
                }
            },
            "membership4": {
                "project": {
                    "id": 1011,
                    "name": "someproject2"
                },
                "roles": {
                    "name": "Участник"
                }
            }
        }
    }
}

def fixed_code():
    projects_ids = {}
    for membership in user.get('user', {}).get('memberships', {}).values():
        if list(filter(lambda role_name: role_name != 'Участник', membership.get('roles', {}).values())):
            project_id = membership.get('project', {}).get('id', None)
            projects_ids[project_id] = 1
    
    return projects_ids

def optimized_code():
    projects_ids = {}

    memberships = user.get('user', {}).get('memberships', {}).values()
    project_id = lambda membership: membership.get('project', {}).get('id', None)

    def get_role_names(membership, predicate):
        return [role for role in membership.get('roles', {}).values() if predicate(role)]

    projects_ids = {project_id(membership):1 for membership in memberships
                    if get_role_names(membership, lambda role: role != 'Участник')}

    return projects_ids

try:
    assert fixed_code() == {123:1,789:1}, "Test fixed_code failed"
    print("Test fixed_code passed!!!")
    
    assert optimized_code() == {123:1,789:1}, "Test optimized_code failed"
    print("Test optimized_code passed!!!")
except AssertionError as e:
    print(e)