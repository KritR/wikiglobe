defmodule WikiglobeWeb.Router do
  use WikiglobeWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api/v1", WikiglobeWeb do
    pipe_through :api

    get "/events", WikiDataController, :index_events
    get "/earthquakes", WikiDataController, :index_earthquakes
  end
end
