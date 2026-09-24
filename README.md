# Project 1: Personal Task Manager (Todo API)

## Goal

Solidify CRUD + response models + relationships.

## Core features

* Models: `User`, `Task` (title, description, completed, priority, due_date, owner_id)
* Endpoints:
  * Create / list / get / update / delete tasks
  * Filter by completed status and priority
  * Assign tasks to a user
* Use proper response models (e.g. `TaskRead`, `TaskCreate`, `TaskUpdate`)
* Soft delete or a `deleted_at` field (optional challenge)

### Stretch challenges

1. Add pagination (`skip` + `limit`) and return a response that includes total count.
2. Add a `completed_at` timestamp that is set automatically when a task is marked done.
3. Return a nested response that includes the owner’s name inside every task.
