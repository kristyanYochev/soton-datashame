const URL_PREFIX = "http://localhost:8080"

export async function callApi(path: string): Promise<any> {
    const url = new URL(path, URL_PREFIX)
    const response = await fetch(url);
    const data = await response.json();
    return data;
}