# Debug Notes

## My debug rule

1. Test the API/backend first.
2. Check the browser network tab.
3. Check the `uvicorn` terminal for traceback errors.
4. Fix the code only after I know where the error is.

## Quick meaning of status codes

- `200` = request works
- `404` = URL or route not found
- `500` = backend code failed

## My order in this project

1. `service.py`
2. `controller.py`
3. `routes/*.py`
4. `/docs`
5. `HTML`
6. `JavaScript`

## Simple workflow

1. Open `/docs` and test the endpoint.
2. Open `F12` in the browser.
3. Check `Network`.
4. If `404`: check `fetch(...)` URL or route name.
5. If `500`: check the `uvicorn` terminal traceback.
6. Fix the exact file where the error starts.

## My shortcut

```text
docs -> network -> terminal -> code fix
```
