import asyncio
from datetime import datetime
from typing import Any, Tuple
from skyvern.forge.sdk.schemas.tasks import Task, TaskStatus
from skyvern.forge.sdk.schemas.tasks import ProxyLocation, Task

# from skyvern.webeye.browser_manager import BrowserManager
from skyvern.webeye.scraper.scraper import scrape_website

from chat_invest.web.browser_manager import BrowserManager

BROWSER_MANAGER = BrowserManager()


async def scrape_url(url: str):
    task = Task(
        task_id="hello",
        status=TaskStatus.created,
        created_at=datetime.now(),
        modified_at=datetime.now(),
        url=url,
        # webhook_callback_url=task_obj.webhook_callback_url,
        # navigation_goal=task_obj.navigation_goal,
        # data_extraction_goal=task_obj.data_extraction_goal,
        # navigation_payload=task_obj.navigation_payload,
        extracted_information=None,
        failure_reason=None,
        # organization_id=task_obj.organization_id,
        # proxy_location=(
        #     ProxyLocation(task_obj.proxy_location) if task_obj.proxy_location else None
        # ),
        # extracted_information_schema=task_obj.extracted_information_schema,
        # workflow_run_id=task_obj.workflow_run_id,
        # order=task_obj.order,
        # retry=task_obj.retry,
        # max_steps_per_run=task_obj.max_steps_per_run,
        # error_code_mapping=task_obj.error_code_mapping,
        # errors=task_obj.errors,
    )

    browser_state = await BROWSER_MANAGER.get_or_create_for_task(task)
    scraped_page = await scrape_website(browser_state, task.url)

    return scraped_page


async def main():
    scraped_page = await scrape_url(url="https://example.com/")

    print(scraped_page)


if __name__ == "__main__":
    asyncio.run(main())
